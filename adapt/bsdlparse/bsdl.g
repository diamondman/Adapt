grammar bsdl;

options {
  language=Python3;
}

evaluate 
    : (entity) EOF;

entity
    :
      ENTITY ename=identifier IS 
    (g=generic SCOLON)+

    port_list SCOLON 

    (use SCOLON)*

    (
      (
        attribute 
        |constant 
      ) SCOLON 
    )*

    END identifier SCOLON //Just assume it is fine
    ;

generic
    : GENERIC OPAREN 
        (gk=identifier COLON identifier
            COLON EQUAL gv=string )
      CPAREN 
    ;

use
    : USE id1=identifier DOT ALL
    ;

attribute
    : ATTRIBUTE 
        atn=identifier OF entn=identifier COLON
        v=general_attribute_assignment
    ;

general_attribute_assignment
    : (ENTITY IS 
            (
                v=identifier
                |v=string
                |v=number
            )
      ) 
      |(SIGNAL IS 
            (
                v=boolean|
                (OPAREN v=scinot_number
                    COMMA BOTH CPAREN)
            )
      ) 
    ;

boolean
    : TRUE|FALSE
    ;

number
    : DIGIT+ 
    ;

constant
    : CONSTANT k=identifier  COLON identifier 
        COLON EQUAL v=string 
    ;

port_list
    : 
        PORT OPAREN 
        (pd=port_def  SCOLON)* 
        (pd=port_def )
        CPAREN;

port_def
    :
       (pname=identifier COMMA)*
        pname=identifier COLON portmode  
        (BIT|
         BIT_VECTOR OPAREN DIGIT+ TO DIGIT+ CPAREN);

identifier 
    : (FULLCASE_WORD|WORD) (FULLCASE_WORD|WORD|DIGIT)* ('_' (FULLCASE_WORD|WORD|DIGIT)+)* 
    ;

portmode
    : IN|OUT|INOUT|BUFFER|LINKAGE|BUS;

string
    : 
      (STRING ANDSIGN )* STRING 
    ;

scinot_number
    : DIGIT* DOT DIGIT* 'e' '+'? DIGIT*
    ;




STRING :   '"' (~'"')* '"';

WHITESPACE
    : ( ' ' | '\t' | '\r' | '\n' )+ -> channel(HIDDEN)
    ;
COMMENT
    :  '--' ~( '\r' | '\n' )* -> channel(HIDDEN)
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

