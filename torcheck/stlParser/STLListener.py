# Generated from STL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .STLParser import STLParser
else:
    from STLParser import STLParser

# This class defines a complete listener for a parse tree produced by STLParser.
class STLListener(ParseTreeListener):

    # Enter a parse tree produced by STLParser#prog.
    def enterProg(self, ctx:STLParser.ProgContext):
        pass

    # Exit a parse tree produced by STLParser#prog.
    def exitProg(self, ctx:STLParser.ProgContext):
        pass


    # Enter a parse tree produced by STLParser#textformula.
    def enterTextformula(self, ctx:STLParser.TextformulaContext):
        pass

    # Exit a parse tree produced by STLParser#textformula.
    def exitTextformula(self, ctx:STLParser.TextformulaContext):
        pass


    # Enter a parse tree produced by STLParser#assign.
    def enterAssign(self, ctx:STLParser.AssignContext):
        pass

    # Exit a parse tree produced by STLParser#assign.
    def exitAssign(self, ctx:STLParser.AssignContext):
        pass


    # Enter a parse tree produced by STLParser#blank.
    def enterBlank(self, ctx:STLParser.BlankContext):
        pass

    # Exit a parse tree produced by STLParser#blank.
    def exitBlank(self, ctx:STLParser.BlankContext):
        pass


    # Enter a parse tree produced by STLParser#AndOr.
    def enterAndOr(self, ctx:STLParser.AndOrContext):
        pass

    # Exit a parse tree produced by STLParser#AndOr.
    def exitAndOr(self, ctx:STLParser.AndOrContext):
        pass


    # Enter a parse tree produced by STLParser#Not.
    def enterNot(self, ctx:STLParser.NotContext):
        pass

    # Exit a parse tree produced by STLParser#Not.
    def exitNot(self, ctx:STLParser.NotContext):
        pass


    # Enter a parse tree produced by STLParser#Atom.
    def enterAtom(self, ctx:STLParser.AtomContext):
        pass

    # Exit a parse tree produced by STLParser#Atom.
    def exitAtom(self, ctx:STLParser.AtomContext):
        pass


    # Enter a parse tree produced by STLParser#parensFormula.
    def enterParensFormula(self, ctx:STLParser.ParensFormulaContext):
        pass

    # Exit a parse tree produced by STLParser#parensFormula.
    def exitParensFormula(self, ctx:STLParser.ParensFormulaContext):
        pass


    # Enter a parse tree produced by STLParser#trueFalse.
    def enterTrueFalse(self, ctx:STLParser.TrueFalseContext):
        pass

    # Exit a parse tree produced by STLParser#trueFalse.
    def exitTrueFalse(self, ctx:STLParser.TrueFalseContext):
        pass


    # Enter a parse tree produced by STLParser#U.
    def enterU(self, ctx:STLParser.UContext):
        pass

    # Exit a parse tree produced by STLParser#U.
    def exitU(self, ctx:STLParser.UContext):
        pass


    # Enter a parse tree produced by STLParser#F.
    def enterF(self, ctx:STLParser.FContext):
        pass

    # Exit a parse tree produced by STLParser#F.
    def exitF(self, ctx:STLParser.FContext):
        pass


    # Enter a parse tree produced by STLParser#G.
    def enterG(self, ctx:STLParser.GContext):
        pass

    # Exit a parse tree produced by STLParser#G.
    def exitG(self, ctx:STLParser.GContext):
        pass


    # Enter a parse tree produced by STLParser#number.
    def enterNumber(self, ctx:STLParser.NumberContext):
        pass

    # Exit a parse tree produced by STLParser#number.
    def exitNumber(self, ctx:STLParser.NumberContext):
        pass


    # Enter a parse tree produced by STLParser#NegNumber.
    def enterNegNumber(self, ctx:STLParser.NegNumberContext):
        pass

    # Exit a parse tree produced by STLParser#NegNumber.
    def exitNegNumber(self, ctx:STLParser.NegNumberContext):
        pass


    # Enter a parse tree produced by STLParser#id.
    def enterId(self, ctx:STLParser.IdContext):
        pass

    # Exit a parse tree produced by STLParser#id.
    def exitId(self, ctx:STLParser.IdContext):
        pass


    # Enter a parse tree produced by STLParser#parensExpr.
    def enterParensExpr(self, ctx:STLParser.ParensExprContext):
        pass

    # Exit a parse tree produced by STLParser#parensExpr.
    def exitParensExpr(self, ctx:STLParser.ParensExprContext):
        pass


    # Enter a parse tree produced by STLParser#AlgOp.
    def enterAlgOp(self, ctx:STLParser.AlgOpContext):
        pass

    # Exit a parse tree produced by STLParser#AlgOp.
    def exitAlgOp(self, ctx:STLParser.AlgOpContext):
        pass


    # Enter a parse tree produced by STLParser#timeBounds.
    def enterTimeBounds(self, ctx:STLParser.TimeBoundsContext):
        pass

    # Exit a parse tree produced by STLParser#timeBounds.
    def exitTimeBounds(self, ctx:STLParser.TimeBoundsContext):
        pass


    # Enter a parse tree produced by STLParser#emptyTimeBounds.
    def enterEmptyTimeBounds(self, ctx:STLParser.EmptyTimeBoundsContext):
        pass

    # Exit a parse tree produced by STLParser#emptyTimeBounds.
    def exitEmptyTimeBounds(self, ctx:STLParser.EmptyTimeBoundsContext):
        pass



del STLParser