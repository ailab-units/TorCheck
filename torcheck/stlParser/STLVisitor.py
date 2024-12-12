# Generated from STL.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .STLParser import STLParser
else:
    from STLParser import STLParser

# This class defines a complete generic visitor for a parse tree produced by STLParser.

class STLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by STLParser#textFormula.
    def visitTextFormula(self, ctx:STLParser.TextFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#plainFormla.
    def visitPlainFormla(self, ctx:STLParser.PlainFormlaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#blank.
    def visitBlank(self, ctx:STLParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#AndOr.
    def visitAndOr(self, ctx:STLParser.AndOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#Not.
    def visitNot(self, ctx:STLParser.NotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#Atom.
    def visitAtom(self, ctx:STLParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#parensFormula.
    def visitParensFormula(self, ctx:STLParser.ParensFormulaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#U.
    def visitU(self, ctx:STLParser.UContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#F.
    def visitF(self, ctx:STLParser.FContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#G.
    def visitG(self, ctx:STLParser.GContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#atomicPredicate.
    def visitAtomicPredicate(self, ctx:STLParser.AtomicPredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#timeBounds.
    def visitTimeBounds(self, ctx:STLParser.TimeBoundsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#rightUnbound.
    def visitRightUnbound(self, ctx:STLParser.RightUnboundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#emptyTimeBounds.
    def visitEmptyTimeBounds(self, ctx:STLParser.EmptyTimeBoundsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#number.
    def visitNumber(self, ctx:STLParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#negNumber.
    def visitNegNumber(self, ctx:STLParser.NegNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#natural.
    def visitNatural(self, ctx:STLParser.NaturalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by STLParser#negNatural.
    def visitNegNatural(self, ctx:STLParser.NegNaturalContext):
        return self.visitChildren(ctx)



del STLParser