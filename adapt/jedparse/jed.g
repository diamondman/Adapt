grammar jed;

options {
  language=Python;
  backtrack=false;
  memoize=false;
}

@header {
import os
import sys
from bitarray import bitarray
}

@init{
    self._fuse_count = 0
    self._fuses = bitarray()
    self._fuse_default = False
    self._pin_count = 0
}

@members{

}

eval returns [value]
    : (otherstar|NL)*
        (entity {$value = $entity.value})
        (otherstar|NL)*
        EOF;

other
    : (OTHER|ZERO|ONE|DIG01|F|J|L|N|P|Q|V|X|WS|C)
    ;

otherstar
    : (other|STAR)
    ;

string 
    : other+
    ;

entity returns [value]
    : STX lines ETX {$value=$lines.value}
    ;

lines returns [value]
    : (  fuse_count     {self._fuse_count = $fuse_count.value}
        |pin_count      {self._pin_count = $pin_count.value}
        |default_fuse
        |default_test
        |test_vec_max
        |fuses
        |note
        |dev_id
        |checksum       {self._checksum = $checksum.value}
      )+
      {
      addr_diff = self._fuse_count-len(self._fuses)
      if addr_diff < 0:
          raise Exception("JEDEC File has more bits than the F field specifies. Actual: \%s; F: \%s."\%\
                          (len(self._fuses), self._fuse_count))
      if addr_diff:
          buff = bitarray(addr_diff)
          buff.setall(self._fuse_default)
          self._fuses += buff
      $value = {'fuses': self._fuses, 
                'checksum': self._checksum, 
                'fusecount': self._fuse_count,
                'pincount': self._pin_count}
      }
    ;

fuses returns [address, length]
    : L digits WS+ bit_field STAR NL {$address=$digits.value}{$length=len($bit_field.text)}
        {
            addr_diff = $address-len(self._fuses)
            if addr_diff<0:
                raise Exception("JED FILE CAN NOT HAVE OUT OF ORDER ADDRESSES!")
            if addr_diff:
                buff = bitarray(addr_diff)
                buff.setall(self._fuse_default)
                self._fuses += buff
            self._fuses += $bit_field.value
        }
    ;

bit_field returns [value]
    : (ZERO|ONE)+ {$value=bitarray(str($bit_field.text))}
    ;

note returns [value]
    : N string STAR NL
        {$value=$string.text}
    ;

checksum returns [value]
    : C string STAR NL
        {$value=$string.text}
    ;

dev_id returns [value]
    : J string STAR NL 
        {$value=$string.text}
    ;

fuse_count returns [value]
    : Q F digits STAR NL {$value=$digits.value}
    ;

pin_count returns [value]
    : Q P digits STAR NL {$value=$digits.value}
    ;

default_fuse returns [value]
    : F bool STAR NL {$value=$bool.value}
        {self._fuse_default=$bool.value}
    ;

default_test returns [value]
    : X bool STAR NL {$value=$bool.value}
    ;

test_vec_max returns [value]
    : Q V bool STAR NL {$value=$bool.value}
    ;

bool returns [value]
    : (ZERO {$value=False}|ONE {$value=True})
    ;

digits returns [value]
    : digit+ {$value = int($digits.text)}
    ;

digit
    : ZERO|ONE|DIG01
    ;

STX    : '\u0002' ;
ETX    : '\u0003' ;
NL     : ('\r' | '\n' )+ ;
C      : 'C' ;
F      : 'F' ;
J      : 'J' ;
L      : 'L' ;
N      : 'N' ;
P      : 'P' ;
Q      : 'Q' ;
V      : 'V' ;
X      : 'X' ;

ONE    : '1' ;
ZERO   : '0' ;
DIG01  : '2'..'9' ;
STAR   : '*' ;
WS     : ' '|'\t';

OTHER : ~('\u0002'|'\u0003') ;

