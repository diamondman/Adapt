import os
import json
from bitarray import bitarray

from bsdlparse import parse_file
from jtagUtils import manufacturer_lookup
from jtagUtils import adapt_base_dir

class DeviceRegister(object):
    def __init__(self, name, length):
        self.name = name
        self.length = int(length)

    def __repr__(self):
        return "<Register(%s; %s bits)>"%(self.name, self.length)

class BSDLInvalidFormatException(Exception):
    pass

class JTAGDeviceDescription(object):
    """Represents a bsdl file which can be used to describe one or more chips
    in a scan chain. Creating an instance of this class parses the bsdl file
    and is necessary to check if the bsdl file applies to the device in question.

    It is highly likely that if you are thinking of creating instances of this class
    outside of the file it is defined in, that you are doing it wrong. Call the
    static get_descriptor_for_idcode method on this class to search for the correct
    descriptor for an idcode."""
    _desc_cache = {}
    _desc_id_file_cache = {}

    def __init__(self, bsdl_path):
        self._file_name = bsdl_path
        parser_result = parse_file(self._file_name)
        #import ipdb
        #ipdb.set_trace()
        self._device_name = parser_result['entity_name']
        attributes = parser_result['attributes']

        if 'IDCODE_REGISTER' not in attributes:
            raise Exception('BSDL files must provide the IDCODE_REGISTER register.')

        idcode = attributes.get('IDCODE_REGISTER', None)
        self._idcode = None
        self._idcode_mask = None
        self._manufacturer_id = None
        if idcode:
            self._idcode = int(idcode.replace('X','0'), 2)
            #Seems this mask is basically constant.
            self._idcode_mask = 0x0FFFFFFF #int(idcode.replace('0', '1').replace('X', '0'), 2)
            #Get the manufacturer id in lower 11 bits but not last
            self._manufacturer_id = (self._idcode>>1) & 0b11111111111

        if 'INSTRUCTION_LENGTH' not in attributes:
            raise Exception('BSDL files must provide the INSTRUCTION_LENGTH of the chain entry')
        self._instruction_length = attributes['INSTRUCTION_LENGTH']

        try:
            instructions_str = attributes['INSTRUCTION_OPCODE'].replace('\t','').replace(' ','')
            instructions_temp = [i.replace(')','').split('(') for i in instructions_str.split('),')]
            self._instructions = {i[0]:bitarray(str(i[1])) for i in instructions_temp 
                                  if ',' not in i[1]}
        except ValueError as e:
            raise BSDLInvalidFormatException('Instruction codes are poorly formatted in %s.'%self._file_name)

        try:
            register_access_str = attributes['REGISTER_ACCESS'].replace('\t','').replace(' ','')
            register_access_temp = [i.replace(')','').split('(') 
                                    for i in register_access_str.split('),')]
            registers_strs = {i[0] for i in register_access_temp if ',' not in i[1]}
            
            try:
                registers_strs.remove("BYPASS")
                registers_strs.remove("BOUNDARY")
            except KeyError as e:
                raise Exception("Register Access configuration does not contain a "
                                "required '%s' register in file %s."%(str(e), self._file_name))

            self.register_map = {
                "BYPASS": DeviceRegister("BYPASS", 1),
                "BOUNDARY": DeviceRegister("BOUNDARY", attributes['BOUNDARY_LENGTH']),
                "IDREGISTER": DeviceRegister("IDREGISTER", 32)
                }

            for reg in registers_strs:
                if '[' not in reg or ']' not in reg:
                    raise Exception("Custom register names in bsdl files must have lengths. "
                                    "Invalid length in file %s, reg %s"%(self._file_name, reg))
                braceindex = reg.index('[')
                endbraceindex = reg.index(']')
                name = reg[:braceindex]
                length = reg[braceindex+1:endbraceindex]
                self.register_map[reg] = DeviceRegister(name, length)

            #TODO Maybe add stuff for idcode into the instruction or check for missing.
            self._ins_reg_map = {i[1]:self.register_map[i[0]] 
                                 for i in register_access_temp if ',' not in i[1]}
        except ValueError as e:
            raise BSDLInvalidFormatException('Register access poorly formatted in %s.'%self._file_name)

        constants_keys = list(parser_result['constants'].keys())
        self._chip_package = "UNKNOWN" if not len(constants_keys) else constants_keys[0];



    @property
    def manufacturer(self):
        return manufacturer_lookup.get(self._manufacturer_id, "UNKNOWN!")

    def does_descriptor_apply_to_idcode(self, code):
        #print(bin(self._idcode_mask&code), bin(self._idcode))
        return (self._idcode_mask&code)==self._idcode

    @classmethod
    def _save_id_file_cache(cls):
        f = open(os.path.join(adapt_base_dir, 'tmp', 'id_bsdl_cache.json'), 'w')
        #print("ABOUT TO DUMP", cls._desc_id_file_cache)
        json.dump(cls._desc_id_file_cache, f)
        f.close()

    @classmethod
    def _load_id_file_cache(cls):
        if len(cls._desc_id_file_cache.keys()) > 0:
            return
        path = os.path.join(adapt_base_dir, 'tmp', 'id_bsdl_cache.json')
        #print(path)
        if os.path.isfile(path):
            try:
                f = open(path)
                fj = json.load(f)
                f.close()
                for did, fn in fj.items():
                    #print("LOADING %s:%s"%(did, fn))
                    cls._desc_id_file_cache[did] = fn
            except:
                print("There was a problem loading the bsdl cache.")

    @classmethod
    def get_descriptor_for_idcode(cls, idcode):
        """Use this method to find bsdl descriptions for devices.
        The caching on this method drastically lower the execution
        time when there are a lot of bsdl files and more than one
        device. May move it into a metaclass to make it more
        transparent."""
        idcode = idcode&0x0fffffff

        #import ipdb
        #ipdb.set_trace()
        cls._load_id_file_cache()
        #ipdb.set_trace()

        #print(cls._desc_id_file_cache.keys())
        if str(idcode) in cls._desc_id_file_cache.keys():
            fname = cls._desc_id_file_cache[str(idcode)]
            desc = JTAGDeviceDescription(fname)
            cls._desc_cache[fname] = desc
            return desc
        print("COULD NOT FIND ID %s" % idcode)
        base_bsdl_dir = os.path.join(adapt_base_dir, 'res', 'bsdl')
        bsdl_files = [os.path.join(dp, f) for dp, dn, filenames in
                      os.walk(base_bsdl_dir) for f in filenames
                      if os.path.splitext(f)[1] in ['.bsd','.bsdl']]
        for fname in bsdl_files:
            if fname in cls._desc_cache:
                desc = cls._desc_cache[fname]
            else:
                desc = JTAGDeviceDescription(fname)
                cls._desc_cache[fname] = desc
                cls._desc_id_file_cache[desc._idcode] = fname
                #print("SAVING")
                cls._save_id_file_cache()
            if desc.does_descriptor_apply_to_idcode(idcode):
                return desc
