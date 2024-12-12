# Generated from STL.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .STLParser import STLParser
else:
    from STLParser import STLParser

# This class defines a complete listener for a parse tree produced by STLParser.
class STLListener(ParseTreeListener):

    # Enter a parse tree produced by STLParser#textFormula.
    def enterTextFormula(self, ctx:STLParser.TextFormulaContext):
        pass

    # Exit a parse tree produced by STLParser#textFormula.
    def exitTextFormula(self, ctx:STLParser.TextFormulaContext):
        pass


    # Enter a parse tree produced by STLParser#plainFormla.
    def enterPlainFormla(self, ctx:STLParser.PlainFormlaContext):
        pass

    # Exit a parse tree produced by STLParser#plainFormla.
    def exitPlainFormla(self, ctx:STLParser.PlainFormlaContext):
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


    # Enter a parse tree produced by STLParser#atomicPredicate.
    def enterAtomicPredicate(self, ctx:STLParser.AtomicPredicateContext):
        pass

    # Exit a parse tree produced by STLParser#atomicPredicate.
    def exitAtomicPredicate(self, ctx:STLParser.AtomicPredicateContext):
        pass


    # Enter a parse tree produced by STLParser#timeBounds.
    def enterTimeBounds(self, ctx:STLParser.TimeBoundsContext):
        pass

    # Exit a parse tree produced by STLParser#timeBounds.
    def exitTimeBounds(self, ctx:STLParser.TimeBoundsContext):
        pass


    # Enter a parse tree produced by STLParser#rightUnbound.
    def enterRightUnbound(self, ctx:STLParser.RightUnboundContext):
        pass

    # Exit a parse tree produced by STLParser#rightUnbound.
    def exitRightUnbound(self, ctx:STLParser.RightUnboundContext):
        pass


    # Enter a parse tree produced by STLParser#emptyTimeBounds.
    def enterEmptyTimeBounds(self, ctx:STLParser.EmptyTimeBoundsContext):
        pass

    # Exit a parse tree produced by STLParser#emptyTimeBounds.
    def exitEmptyTimeBounds(self, ctx:STLParser.EmptyTimeBoundsContext):
        pass


    # Enter a parse tree produced by STLParser#number.
    def enterNumber(self, ctx:STLParser.NumberContext):
        pass

    # Exit a parse tree produced by STLParser#number.
    def exitNumber(self, ctx:STLParser.NumberContext):
        pass


    # Enter a parse tree produced by STLParser#negNumber.
    def enterNegNumber(self, ctx:STLParser.NegNumberContext):
        pass

    # Exit a parse tree produced by STLParser#negNumber.
    def exitNegNumber(self, ctx:STLParser.NegNumberContext):
        pass


    # Enter a parse tree produced by STLParser#natural.
    def enterNatural(self, ctx:STLParser.NaturalContext):
        pass

    # Exit a parse tree produced by STLParser#natural.
    def exitNatural(self, ctx:STLParser.NaturalContext):
        pass


    # Enter a parse tree produced by STLParser#negNatural.
    def enterNegNatural(self, ctx:STLParser.NegNaturalContext):
        pass

    # Exit a parse tree produced by STLParser#negNatural.
    def exitNegNatural(self, ctx:STLParser.NegNaturalContext):
        pass



del STLParser