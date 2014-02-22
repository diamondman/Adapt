grammar bsdl;

options {
  language=Python;
  backtrack=false;
  memoize=false;
}

@header {
import os
import sys
}

@init{
    self.attributes = {}
    self.chip_package = None
    self.ports = []
}

@members{

}

eval returns [value]
    : (entity){$value=$entity.value}
        EOF;

entity returns [value]
    : {$value = {}}
      ENTITY ename=identifier IS 
        {$value['entity_name'] = $ename.value}

    {$value['generics']={}}
    (g=generic SCOLON {$value['generics'][$g.key]=$g.value})+

    port_list SCOLON 
        {$value['ports']=$port_list.value}

    (use SCOLON)*

    {$value['attributes']={}}
    {$value['constants']={}}
    (
      (
        (i=attribute {$value['attributes'][$i.key]=$i.value})
        |(i=constant {$value['constants'][$i.key]=$i.value})
      ) SCOLON 
    )*

    END identifier SCOLON //Just assume it is fine
    ;

generic returns [key, value]
    : GENERIC OPAREN 
        (gk=identifier COLON identifier
            COLON EQUAL gv=string )
      CPAREN {$value=$gv.value}{$key=$gk.value}
    ;

use
    : USE id1=identifier DOT ALL
        {#oprint $id1.text+".all"}
    ;

attribute returns [key, value]
    : ATTRIBUTE 
        atn=identifier OF entn=identifier COLON {$key=$atn.value} 
        {#print "ATTRIBUTE CREATION", $atn.value, $entn.value} 
        v=general_attribute_assignment {$value=$v.value}
    ;

general_attribute_assignment returns [value]
    : (ENTITY IS 
            (
                i=identifier {$value=$i.value}
                |s=string {$value=$s.value}
                |n=number {$value=$n.value}
            )
      )
      |(SIGNAL IS 
            (
                (TRUE {$value=True}|FALSE {$value=False})|
                (OPAREN scinot_number {$value=$scinot_number.text}
                    COMMA BOTH CPAREN)
            )
      )
    ;

number returns [value]
    : DIGIT+ {$value=int($number.text)}
    ;

constant returns [key, value]
    : CONSTANT k=identifier {$key=$k.value} COLON identifier 
        COLON EQUAL v=string {$value=$v.value}
    ;

port_list returns [value]
    : {value = []}
        PORT OPAREN 
        (pd=port_def {value.extend($pd.value)} SCOLON)* 
        (pd=port_def {value.extend($pd.value)})
        CPAREN;

port_def returns [value]
    : {$value=[]}
       (pname=identifier {$value.append($pname.value)} COMMA)*
        pname=identifier {$value.append($pname.value)} COLON portmode  
        (BIT|
         BIT_VECTOR OPAREN DIGIT+ TO DIGIT+ CPAREN);

identifier returns [value]
    : (FULLCASE_WORD|WORD) (FULLCASE_WORD|WORD|DIGIT)* ('_' (FULLCASE_WORD|WORD|DIGIT)+)* {$value = $identifier.text.upper()}
    ;

portmode returns [value]
    : IN|OUT|INOUT|BUFFER|LINKAGE|BUS;

string returns [value]
    : {str_parts = []}
      (s=STRING ANDSIGN {str_parts.append($s.text[1:-1])})* 
        s1=STRING {str_parts.append($s1.text[1:-1])}
        {$value = "".join(str_parts)}
    ;

scinot_number
    : DIGIT* DOT DIGIT* 'e' '+'? DIGIT*
    ;




STRING :   '"' (~'"')* '"';

WHITESPACE
    : ( ' ' | '\t' | '\r' | '\n' )+ { $channel = HIDDEN }
    ;
COMMENT
    :  '--' ~( '\r' | '\n' )* { $channel = HIDDEN }
    ;

ANDSIGN         : '&';
USCORE          : '_';
OPAREN          : '(';
CPAREN          : ')';
COLON           : ':';
SCOLON          : ';';
EQUAL           : '=';
COMMA           : ',';
DOT             : '.';

BIT             :    'bit';
BIT_VECTOR      :    'bit_vector';

ABS             :    'abs';
ACCESS          :    'access';
AFTER           :    'after';
ALIAS           :    'alias';
ALL             :    'all';
AND             :    'and';
ARCHITECTURE    :    'architecture';
ARRAY           :    'array';
ASSERT          :    'assert';
ATTRIBUTE       :    'attribute';
BEGIN           :    'begin';
BLOCK           :    'block';
BODY            :    'body';
BUFFER          :    'buffer';
BUS             :    'bus';
CASE            :    'case';
COMPONENT       :    'component';
CONFIGURATION   :    'configuration';
CONSTANT        :    'constant';
DISCONNECT      :    'disconnect';
DOWNTO          :    'downto';
ELSE            :    'else';
ELSIF           :    'elsif';
END             :    'end';
ENTITY          :    'entity';
EXIT            :    'exit';
FILE            :    'file';
FOR             :    'for';
FUNCTION        :    'function';
GENERATE        :    'generate';
GENERIC         :    'generic';
GROUP           :    'group';
GUARDED         :    'guarded';
IF              :    'if';
IMPURE          :    'impure';
IN              :    'in';
INERTIAL        :    'inertial';
INOUT           :    'inout';
IS              :    'is';
LABEL           :    'label';
LIBRARY         :    'library';
LINKAGE         :    'linkage';
LITERAL         :    'literal';
LOOP            :    'loop';
MAP             :    'map';
MOD             :    'mod';
NAND            :    'nand';
NEW             :    'new';
NEXT            :    'next';
NOR             :    'nor';
NOT             :    'not';
NULL            :    'null';
OF              :    'of';
ON              :    'on';
OPEN            :    'open';
OR              :    'or';
OTHERS          :    'others';
OUT             :    'out';
PACKAGE         :    'package';
PORT            :    'port';
POSTPONED       :    'postponed';
PROCEDURE       :    'procedure';
PROCESS         :    'process';
PURE            :    'pure';
RANGE           :    'range';
RECORD          :    'record';
REGISTER        :    'register';
REJECT          :    'reject';
REM             :    'rem';
REPORT          :    'report';
RETURN          :    'return';
ROL             :    'rol';
ROR             :    'ror';
SELECT          :    'select';
SEVERITY        :    'severity';
SIGNAL          :    'signal';
SHARED          :    'shared';
SLA             :    'sla';
SLL             :    'sll';
SRA             :    'sra';
SRL             :    'srl';
SUBTYPE         :    'subtype';
THEN            :    'then';
TO              :    'to';
TRANSPORT       :    'transport';
TYPE            :    'type';
UNAFFECTED      :    'unaffected';
UNITS           :    'units';
UNTIL           :    'until';
USE             :    'use';
VARIABLE        :    'variable';
WAIT            :    'wait';
WHEN            :    'when';
WHILE           :    'while';
WITH            :    'with';
XNOR            :    'xnor';
XOR             :    'xor';

TRUE            :    'true';
FALSE           :    'false';
BOTH            :    'BOTH'|'both';

WORD            : CHAR+ ;
FULLCASE_WORD   : ICHAR+;
fragment CHAR   : 'a'..'z' ;
fragment ICHAR  : (CHAR|'A'..'Z') ;
DIGIT           : '0'..'9' ;

