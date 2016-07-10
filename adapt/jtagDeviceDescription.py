import os
import json
import re
import fnmatch
import numbers
from bitarray import bitarray

from jtagUtils import manufacturer_lookup
from jtagUtils import adapt_base_dir
from utils import memoized

from jtagDeviceDescriptionNetResolver import get_sid, get_details, decode_bsdl

_descr_file_re = re.compile('[01X]'*32+".json")
base_descr_dir = os.path.join(os.path.expanduser("~"),
                              '.config', 'adapt', 'jtag_descr')

def _check_cache_for_idcode(id_str):
    best_file = None
    try:
        for file in os.listdir(base_descr_dir):
            if _descr_file_re.match(file) and\
               re.match(file.strip(".json").replace("X","."), id_str) and\
               (not best_file or best_file.count('X') > file.count('X')):
                best_file = file
    except FileNotFoundError:
        pass
    if best_file:
        return os.path.join(base_descr_dir, best_file)

@memoized
def get_descriptor_for_idcode(idcode):
    """Use this method to find bsdl descriptions for devices.
    The caching on this method drastically lower the execution
    time when there are a lot of bsdl files and more than one
    device. May move it into a metaclass to make it more
    transparent."""
    idcode = idcode&0x0fffffff
    id_str = "XXXX"+bin(idcode)[2:].zfill(28)

    descr_file_path = _check_cache_for_idcode(id_str)
    if descr_file_path:
        with open(descr_file_path, 'r') as f:
            dat = json.load(f)
        return JTAGDeviceDescription(dat.get('idcode'), dat.get('name'),
                                     dat.get('ir_length'),
                                     dat.get('instruction_opcodes'))

    print("    Device detected ("+id_str+"). Fetching missing descriptor...")
    sid = get_sid(id_str)
    details = get_details(sid)
    attribs = decode_bsdl(sid)

    #for k,v in attribs.items():
    #    if k != "BOUNDARY_REGISTER" and k != "DESIGN_WARNING":
    #        print("\033[1m"+k+"\033[0m",":",type(v).__name__+"("+str(v)+")")

    instruction_length = 0
    if attribs.get('INSTRUCTION_LENGTH') ==\
       details.get('INSTRUCTION_LENGTH'):
        instruction_length = attribs.get('INSTRUCTION_LENGTH')
    elif attribs.get('INSTRUCTION_LENGTH') and\
       details.get('INSTRUCTION_LENGTH'):
        raise Exception("INSTRUCTION_LENGTH can not be determined")
    elif attribs.get('INSTRUCTION_LENGTH'):
        instruction_length = attribs.get('INSTRUCTION_LENGTH')
    else:
        instruction_length = details.get('INSTRUCTION_LENGTH')

    for instruction_name in details.get('instructions'):
        if instruction_name not in\
           attribs.get('INSTRUCTION_OPCODE',[]):
            raise Exception("INSTRUCTION_OPCODE sources do not match")

    #print(attribs['IDCODE_REGISTER'])
    descr = JTAGDeviceDescription(attribs['IDCODE_REGISTER'].upper(),
                                  details['name'], instruction_length,
                                  attribs['INSTRUCTION_OPCODE'])

    #CACHE DESCR AS FILE!
    if not os.path.isdir(base_descr_dir):
        os.makedirs(base_descr_dir)
    descr_file_path = os.path.join(base_descr_dir,
                                   attribs['IDCODE_REGISTER']\
                                   .upper()+'.json')
    with open(descr_file_path, 'w') as f:
        json.dump(descr._dump(), f)

    return descr


class JTAGDeviceDescription(object):
    def __init__(self, idcode, name, ir_length, instruction_opcodes):
        if isinstance(idcode, numbers.Number):
            self._idcode = idcode
            self._idcode_mask = 0x0FFFFFFF
            self._idcode_str = "XXXX"+bin(idcode)[2:].zfill(28)
        else:
            self._idcode = int(idcode.upper().replace('X','0'), 2)
            self._idcode_mask = int(idcode.replace('0', '1').replace('X', '0'), 2)
            self._idcode_str = idcode.upper()

        if not self._idcode&1:
            raise Exception("Invalid JTAG ID Code")
        self._manufacturer_id = (self._idcode & 0b111111111110)>>1
        self._product_id = (self._idcode & 0x0FFFF000)>>12
        self._version = (self._idcode & 0xF0000000)>>28

        self._device_name = name
        self._chip_package = "UNKNOWN"

        if not isinstance(ir_length, int) or ir_length < 1:
            raise Exception('BSDL files must provide the INSTRUCTION_LENGTH of the chain entry')
        self._ir_length = ir_length

        #TODO Add checks to make sure the instruction lengths are sane
        self._instructions = {k:bitarray(v) for k,v in instruction_opcodes.items()}

    def _dump(self):
        return {
            'idcode': self._idcode_str,
            'name': self._device_name,
            'ir_length': self._ir_length,
            'instruction_opcodes':
            {k:"".join(["1" if tf else "0" for tf in v.tolist()])
             for k,v in self._instructions.items()}
            }

    @property
    def manufacturer(self):
        return manufacturer_lookup.get(self._manufacturer_id, "UNKNOWN!")

    def does_descriptor_apply_to_idcode(self, code):
        #print(bin(self._idcode_mask&code), bin(self._idcode))
        return (self._idcode_mask&code)==self._idcode
