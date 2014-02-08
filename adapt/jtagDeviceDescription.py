import os

from bsdlparse import parse_file
from jtagUtils import manufacturer_lookup

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

    def __init__(self, bsdl_path):
        self._file_name = bsdl_path
        parser_result = parse_file(self._file_name)
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
            self._idcode_mask = int(idcode.replace('0', '1').replace('X', '0'), 2)
            #Get the manufacturer id in lower 11 bits but not last
            self._manufacturer_id = (self._idcode>>1) & 0b11111111111

        if 'INSTRUCTION_LENGTH' not in attributes:
            raise Exception('BSDL files must provide the INSTRUCTION_LENGTH of the chain entry')
        self._instruction_length = attributes['INSTRUCTION_LENGTH']

        try:
            instructions_str = attributes['INSTRUCTION_OPCODE'].replace('\t','').replace(' ','')
            instructions_temp = [i.replace(')','').split('(') for i in instructions_str.split('),')]
            self._instructions = {i[0]:int(i[1], 2) for i in instructions_temp if ',' not in i[1]}
        except ValueError, e:
            raise BSDLInvalidFormatException('Instruction codes are poorly formatted in %s.'%self._file_name)

        constants_keys = parser_result['constants'].keys()
        self._chip_package = "UNKNOWN" if not len(constants_keys) else constants_keys[0];


    @property
    def manufacturer(self):
        return manufacturer_lookup.get(self._manufacturer_id, "UNKNOWN!")

    def does_descriptor_apply_to_idcode(self, code):
        #print bin(self._idcode_mask&code), bin(self._idcode)
        return (self._idcode_mask&code)==self._idcode

    @classmethod
    def get_descriptor_for_idcode(cls, idcode):
        """Use this method to find bsdl descriptions for devices.
        The caching on this method drastically lower the execution
        time when there are a lot of bsdl files and more than one 
        device. May move it into a metaclass to make it more 
        transparent."""
        #print "LOOKING UP!"
        base_bsdl_dir = '../res/bsdl/'
        bsdl_files = [os.path.join(dp, f) for dp, dn, filenames in 
                      os.walk(base_bsdl_dir) for f in filenames 
                      if os.path.splitext(f)[1] in ['.bsd','.bsdl']]
        for fname in bsdl_files:
            if fname in cls._desc_cache:
                desc = cls._desc_cache[fname]
            else:
                desc = JTAGDeviceDescription(fname)
                cls._desc_cache[fname] = desc
            if desc.does_descriptor_apply_to_idcode(idcode):
                return desc
