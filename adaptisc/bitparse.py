import collections
from datetime import datetime
import os
import struct

from proteusisc import bitarray

class BadBitFile(Exception):
    pass

class BitFile(collections.Sequence):
    def __init__(self, path):
        self._path = path
        self._design = None
        self._part = None
        self._data = None
        self._created = None

        filelen = os.path.getsize(self._path)
        with open(self._path, 'rb') as f:
            #http://www.fpga-faq.com/FAQ_Pages/0026_Tell_me_about_bit_files.htm
            #breaking description where 'a' has a length token to make
            #more consistent
            magicval = BitFile.get_header_val(f)
            if magicval != b'\x0f\xf0\x0f\xf0\x0f\xf0\x0f\xf0\x00':
                raise BadBitFile("Bad magic number %s"%magicval)
            unknownlen = BitFile.get_len_short(f) #Maybe flags?
            if unknownlen != 1:
                raise BadBitFile("Unrecognized value for 3rd field %s"%
                                 unknownlen)

            date_part, time_part = None, None
            parsed_fields = set()
            while f.tell() < filelen:
                k, v = BitFile.get_named_header(f)
                if k in parsed_fields:
                    raise BadBitFile("Duplicate field '%s'"%k)
                parsed_fields.add(k)
                if k in ('a','b','c','d'):
                    v = v.decode().replace('\x00','')
                if k == 'a':
                    self._design = v
                elif k == 'b':
                    self._part = v
                elif k == 'c':
                    date_part = v
                elif k == 'd':
                    time_part = v
                elif k == 'e':
                    self._data = v
                else:
                    raise BadBitFile("Invalid header '%s'"%k)

            if date_part is None or time_part is None:
                raise BadBitFile("Bitfile must specify a create date and time.")
            self._created = datetime.strptime("%s %s"%(date_part, time_part),
                                              "%Y/%m/%d %H:%M:%S")
            if parsed_fields != {'a', 'b', 'c', 'd', 'e'}:
                raise BadBitFile("Not all required fields found in file.")

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self._data.__getitem__(index)

    def __repr__(self):
        return "<%s: Size: %s; (%s; %s; %s)>"%(
            type(self).__name__,
            len(self._data),
            self._design,
            self._part,
            self._created)

    def to_bitarray(self):
        res = bitarray()
        res.frombytes(self._data)
        res.reverse()
        return res

    @staticmethod
    def get_len_short(f):
        dat = f.read(2)
        if len(dat) < 2:
            raise EOFError()
        return struct.unpack(">H", dat)[0]

    @staticmethod
    def get_len_int(f):
        dat = f.read(4)
        if len(dat) < 4:
            raise EOFError()
        return struct.unpack(">I", dat)[0]

    @staticmethod
    def get_header_val(f, sizeint=False):
        if sizeint:
            datalen = BitFile.get_len_int(f)
        else:
            datalen = BitFile.get_len_short(f)
        data = f.read(datalen)
        if len(data) < datalen:
            raise EOFError()
        return data

    @staticmethod
    def get_named_header(f):
        headernameraw = f.read(1)
        if len(headernameraw) < 1:
            raise EOFError()
        headername = headernameraw.decode()
        headerval = BitFile.get_header_val(f, sizeint=headername == 'e')
        return headername, headerval
