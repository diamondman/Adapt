# Generated from java-escape by ANTLR 4.4
from antlr4 import *
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .bsdlListener import bsdlListener
else:
    from bsdlListener import bsdlListener

import ipdb

# This class defines a complete listener for a parse tree produced by bsdlParser.
class bsdlListenerImpl(bsdlListener):

    result = None

    # Enter a parse tree produced by bsdlParser#generic.
    def exitGeneric(self, ctx):
        ctx.value = ctx.gv.value
        ctx.key = ctx.gk.value


    # Exit a parse tree produced by bsdlParser#evaluate.
    def exitEvaluate(self, ctx):
        ctx.value = ctx.entity().value
        self.result = ctx.entity().value


    # Enter a parse tree produced by bsdlParser#constant.
    def enterConstant(self, ctx):
        ctx.key = ctx.k.getText()
        ctx.value = ctx.v.getText()


    # Enter a parse tree produced by bsdlParser#port_list.
    def exitPort_list(self, ctx):
        ctx.value = [pd.value for pd in ctx.port_def()]        


    # Exit a parse tree produced by bsdlParser#entity.
    def exitEntity(self, ctx):
        ctx.value = {'entity_name': ctx.ename.value,
                     'generics': {g.key: g.value for g in ctx.generic()},
                     'ports': ctx.port_list().value,
                     'attributes': {a.key: a.value for a in ctx.attribute()},
                     'constants': {c.key: c.value for c in ctx.constant()},
                 }


    # Enter a parse tree produced by bsdlParser#attribute.
    def exitAttribute(self, ctx):
        ctx.key = ctx.atn.value
        ctx.value = ctx.v.value


    # Enter a parse tree produced by bsdlParser#number.
    def enterNumber(self, ctx):
        ctx.value = int(ctx.getText())


    # Exit a parse tree produced by bsdlParser#general_attribute_assignment.
    def exitGeneral_attribute_assignment(self, ctx):
        ctx.value = ctx.v.value


    # Enter a parse tree produced by bsdlParser#string.
    def enterString(self, ctx):
        ctx.value = "".join([s.getText()[1:-1] for s in ctx.STRING()])


    # Enter a parse tree produced by bsdlParser#port_def.
    def exitPort_def(self, ctx):
        ctx.value = [pname.value for pname in ctx.identifier()]


    # Enter a parse tree produced by bsdlParser#identifier.
    def enterIdentifier(self, ctx):
        ctx.value = ctx.getText().upper()


    # Enter a parse tree produced by bsdlParser#boolean.
    def enterBoolean(self, ctx):
        ctx.value = bool(ctx.TRUE())


    # Enter a parse tree produced by bsdlParser#scinot_number.
    def enterScinot_number(self, ctx):
        ctx.value = ctx.getText()
