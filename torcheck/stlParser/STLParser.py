# Generated from STL.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,82,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        0,1,0,3,0,16,8,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,53,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,72,8,3,1,4,1,4,1,4,
        1,4,1,4,1,4,3,4,80,8,4,1,4,0,0,5,0,2,4,6,8,0,2,1,0,14,15,1,0,18,
        19,89,0,15,1,0,0,0,2,52,1,0,0,0,4,54,1,0,0,0,6,71,1,0,0,0,8,79,1,
        0,0,0,10,11,3,2,1,0,11,12,5,21,0,0,12,16,1,0,0,0,13,16,3,2,1,0,14,
        16,5,21,0,0,15,10,1,0,0,0,15,13,1,0,0,0,15,14,1,0,0,0,16,1,1,0,0,
        0,17,18,5,3,0,0,18,19,3,2,1,0,19,20,7,0,0,0,20,21,3,2,1,0,21,22,
        5,4,0,0,22,53,1,0,0,0,23,24,5,16,0,0,24,53,3,2,1,0,25,26,3,4,2,0,
        26,27,7,1,0,0,27,28,3,8,4,0,28,53,1,0,0,0,29,30,5,3,0,0,30,31,3,
        2,1,0,31,32,5,4,0,0,32,53,1,0,0,0,33,34,5,3,0,0,34,35,3,2,1,0,35,
        36,5,8,0,0,36,37,3,6,3,0,37,38,3,2,1,0,38,39,5,4,0,0,39,53,1,0,0,
        0,40,41,5,9,0,0,41,42,3,6,3,0,42,43,5,3,0,0,43,44,3,2,1,0,44,45,
        5,4,0,0,45,53,1,0,0,0,46,47,5,10,0,0,47,48,3,6,3,0,48,49,5,3,0,0,
        49,50,3,2,1,0,50,51,5,4,0,0,51,53,1,0,0,0,52,17,1,0,0,0,52,23,1,
        0,0,0,52,25,1,0,0,0,52,29,1,0,0,0,52,33,1,0,0,0,52,40,1,0,0,0,52,
        46,1,0,0,0,53,3,1,0,0,0,54,55,5,20,0,0,55,56,5,13,0,0,56,57,5,1,
        0,0,57,5,1,0,0,0,58,59,5,6,0,0,59,60,3,8,4,0,60,61,5,5,0,0,61,62,
        3,8,4,0,62,63,5,7,0,0,63,72,1,0,0,0,64,65,5,6,0,0,65,66,3,8,4,0,
        66,67,5,5,0,0,67,68,5,11,0,0,68,69,5,7,0,0,69,72,1,0,0,0,70,72,1,
        0,0,0,71,58,1,0,0,0,71,64,1,0,0,0,71,70,1,0,0,0,72,7,1,0,0,0,73,
        80,5,2,0,0,74,75,5,12,0,0,75,80,5,2,0,0,76,80,5,1,0,0,77,78,5,12,
        0,0,78,80,5,1,0,0,79,73,1,0,0,0,79,74,1,0,0,0,79,76,1,0,0,0,79,77,
        1,0,0,0,80,9,1,0,0,0,4,15,52,71,79
    ]

class STLParser ( Parser ):

    grammarFileName = "STL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "','", "'['", "']'", "'until'", "'eventually'", "'always'", 
                     "'inf'", "'-'", "'_'", "'and'", "'or'", "'not'", "'='", 
                     "'>='", "'<='", "'x'" ]

    symbolicNames = [ "<INVALID>", "NATURAL", "NUMBER", "LPAR", "RPAR", 
                      "COMMA", "LBRAT", "RBRAT", "U", "F", "G", "INF", "MINUS", 
                      "UNDERSCORE", "AND", "OR", "NOT", "EQ", "GE", "LE", 
                      "X", "NEWLINE", "COMMENT", "WS" ]

    RULE_prog = 0
    RULE_formula = 1
    RULE_var = 2
    RULE_interval = 3
    RULE_expr = 4

    ruleNames =  [ "prog", "formula", "var", "interval", "expr" ]

    EOF = Token.EOF
    NATURAL=1
    NUMBER=2
    LPAR=3
    RPAR=4
    COMMA=5
    LBRAT=6
    RBRAT=7
    U=8
    F=9
    G=10
    INF=11
    MINUS=12
    UNDERSCORE=13
    AND=14
    OR=15
    NOT=16
    EQ=17
    GE=18
    LE=19
    X=20
    NEWLINE=21
    COMMENT=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return STLParser.RULE_prog

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(ProgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.ProgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(STLParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlank" ):
                return visitor.visitBlank(self)
            else:
                return visitor.visitChildren(self)


    class PlainFormlaContext(ProgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.ProgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(STLParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlainFormla" ):
                listener.enterPlainFormla(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlainFormla" ):
                listener.exitPlainFormla(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlainFormla" ):
                return visitor.visitPlainFormla(self)
            else:
                return visitor.visitChildren(self)


    class TextFormulaContext(ProgContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.ProgContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(STLParser.FormulaContext,0)

        def NEWLINE(self):
            return self.getToken(STLParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTextFormula" ):
                listener.enterTextFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTextFormula" ):
                listener.exitTextFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTextFormula" ):
                return visitor.visitTextFormula(self)
            else:
                return visitor.visitChildren(self)



    def prog(self):

        localctx = STLParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.state = 15
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                localctx = STLParser.TextFormulaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 10
                self.formula()
                self.state = 11
                self.match(STLParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = STLParser.PlainFormlaContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.formula()
                pass

            elif la_ == 3:
                localctx = STLParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 14
                self.match(STLParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormulaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return STLParser.RULE_formula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NotContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(STLParser.NOT, 0)
        def formula(self):
            return self.getTypedRuleContext(STLParser.FormulaContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot" ):
                listener.enterNot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot" ):
                listener.exitNot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot" ):
                return visitor.visitNot(self)
            else:
                return visitor.visitChildren(self)


    class UContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(STLParser.LPAR, 0)
        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STLParser.FormulaContext)
            else:
                return self.getTypedRuleContext(STLParser.FormulaContext,i)

        def U(self):
            return self.getToken(STLParser.U, 0)
        def interval(self):
            return self.getTypedRuleContext(STLParser.IntervalContext,0)

        def RPAR(self):
            return self.getToken(STLParser.RPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterU" ):
                listener.enterU(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitU" ):
                listener.exitU(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitU" ):
                return visitor.visitU(self)
            else:
                return visitor.visitChildren(self)


    class FContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def F(self):
            return self.getToken(STLParser.F, 0)
        def interval(self):
            return self.getTypedRuleContext(STLParser.IntervalContext,0)

        def LPAR(self):
            return self.getToken(STLParser.LPAR, 0)
        def formula(self):
            return self.getTypedRuleContext(STLParser.FormulaContext,0)

        def RPAR(self):
            return self.getToken(STLParser.RPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterF" ):
                listener.enterF(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitF" ):
                listener.exitF(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitF" ):
                return visitor.visitF(self)
            else:
                return visitor.visitChildren(self)


    class ParensFormulaContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(STLParser.LPAR, 0)
        def formula(self):
            return self.getTypedRuleContext(STLParser.FormulaContext,0)

        def RPAR(self):
            return self.getToken(STLParser.RPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensFormula" ):
                listener.enterParensFormula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensFormula" ):
                listener.exitParensFormula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensFormula" ):
                return visitor.visitParensFormula(self)
            else:
                return visitor.visitChildren(self)


    class GContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.FormulaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def G(self):
            return self.getToken(STLParser.G, 0)
        def interval(self):
            return self.getTypedRuleContext(STLParser.IntervalContext,0)

        def LPAR(self):
            return self.getToken(STLParser.LPAR, 0)
        def formula(self):
            return self.getTypedRuleContext(STLParser.FormulaContext,0)

        def RPAR(self):
            return self.getToken(STLParser.RPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterG" ):
                listener.enterG(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitG" ):
                listener.exitG(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitG" ):
                return visitor.visitG(self)
            else:
                return visitor.visitChildren(self)


    class AndOrContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.FormulaContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(STLParser.LPAR, 0)
        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STLParser.FormulaContext)
            else:
                return self.getTypedRuleContext(STLParser.FormulaContext,i)

        def RPAR(self):
            return self.getToken(STLParser.RPAR, 0)
        def AND(self):
            return self.getToken(STLParser.AND, 0)
        def OR(self):
            return self.getToken(STLParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndOr" ):
                listener.enterAndOr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndOr" ):
                listener.exitAndOr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAndOr" ):
                return visitor.visitAndOr(self)
            else:
                return visitor.visitChildren(self)


    class AtomContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.FormulaContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def var(self):
            return self.getTypedRuleContext(STLParser.VarContext,0)

        def expr(self):
            return self.getTypedRuleContext(STLParser.ExprContext,0)

        def GE(self):
            return self.getToken(STLParser.GE, 0)
        def LE(self):
            return self.getToken(STLParser.LE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)



    def formula(self):

        localctx = STLParser.FormulaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_formula)
        self._la = 0 # Token type
        try:
            self.state = 52
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = STLParser.AndOrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.match(STLParser.LPAR)
                self.state = 18
                self.formula()
                self.state = 19
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==14 or _la==15):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 20
                self.formula()
                self.state = 21
                self.match(STLParser.RPAR)
                pass

            elif la_ == 2:
                localctx = STLParser.NotContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 23
                self.match(STLParser.NOT)
                self.state = 24
                self.formula()
                pass

            elif la_ == 3:
                localctx = STLParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.var()
                self.state = 26
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 27
                self.expr()
                pass

            elif la_ == 4:
                localctx = STLParser.ParensFormulaContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 29
                self.match(STLParser.LPAR)
                self.state = 30
                self.formula()
                self.state = 31
                self.match(STLParser.RPAR)
                pass

            elif la_ == 5:
                localctx = STLParser.UContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 33
                self.match(STLParser.LPAR)
                self.state = 34
                self.formula()
                self.state = 35
                self.match(STLParser.U)
                self.state = 36
                self.interval()
                self.state = 37
                self.formula()
                self.state = 38
                self.match(STLParser.RPAR)
                pass

            elif la_ == 6:
                localctx = STLParser.FContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 40
                self.match(STLParser.F)
                self.state = 41
                self.interval()
                self.state = 42
                self.match(STLParser.LPAR)
                self.state = 43
                self.formula()
                self.state = 44
                self.match(STLParser.RPAR)
                pass

            elif la_ == 7:
                localctx = STLParser.GContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 46
                self.match(STLParser.G)
                self.state = 47
                self.interval()
                self.state = 48
                self.match(STLParser.LPAR)
                self.state = 49
                self.formula()
                self.state = 50
                self.match(STLParser.RPAR)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return STLParser.RULE_var

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AtomicPredicateContext(VarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.VarContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def X(self):
            return self.getToken(STLParser.X, 0)
        def UNDERSCORE(self):
            return self.getToken(STLParser.UNDERSCORE, 0)
        def NATURAL(self):
            return self.getToken(STLParser.NATURAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomicPredicate" ):
                listener.enterAtomicPredicate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomicPredicate" ):
                listener.exitAtomicPredicate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomicPredicate" ):
                return visitor.visitAtomicPredicate(self)
            else:
                return visitor.visitChildren(self)



    def var(self):

        localctx = STLParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var)
        try:
            localctx = STLParser.AtomicPredicateContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(STLParser.X)
            self.state = 55
            self.match(STLParser.UNDERSCORE)
            self.state = 56
            self.match(STLParser.NATURAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntervalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return STLParser.RULE_interval

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class EmptyTimeBoundsContext(IntervalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.IntervalContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmptyTimeBounds" ):
                listener.enterEmptyTimeBounds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmptyTimeBounds" ):
                listener.exitEmptyTimeBounds(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEmptyTimeBounds" ):
                return visitor.visitEmptyTimeBounds(self)
            else:
                return visitor.visitChildren(self)


    class TimeBoundsContext(IntervalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.IntervalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRAT(self):
            return self.getToken(STLParser.LBRAT, 0)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STLParser.ExprContext)
            else:
                return self.getTypedRuleContext(STLParser.ExprContext,i)

        def COMMA(self):
            return self.getToken(STLParser.COMMA, 0)
        def RBRAT(self):
            return self.getToken(STLParser.RBRAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimeBounds" ):
                listener.enterTimeBounds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimeBounds" ):
                listener.exitTimeBounds(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTimeBounds" ):
                return visitor.visitTimeBounds(self)
            else:
                return visitor.visitChildren(self)


    class RightUnboundContext(IntervalContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.IntervalContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LBRAT(self):
            return self.getToken(STLParser.LBRAT, 0)
        def expr(self):
            return self.getTypedRuleContext(STLParser.ExprContext,0)

        def COMMA(self):
            return self.getToken(STLParser.COMMA, 0)
        def INF(self):
            return self.getToken(STLParser.INF, 0)
        def RBRAT(self):
            return self.getToken(STLParser.RBRAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRightUnbound" ):
                listener.enterRightUnbound(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRightUnbound" ):
                listener.exitRightUnbound(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRightUnbound" ):
                return visitor.visitRightUnbound(self)
            else:
                return visitor.visitChildren(self)



    def interval(self):

        localctx = STLParser.IntervalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_interval)
        try:
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = STLParser.TimeBoundsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(STLParser.LBRAT)
                self.state = 59
                self.expr()
                self.state = 60
                self.match(STLParser.COMMA)
                self.state = 61
                self.expr()
                self.state = 62
                self.match(STLParser.RBRAT)
                pass

            elif la_ == 2:
                localctx = STLParser.RightUnboundContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(STLParser.LBRAT)
                self.state = 65
                self.expr()
                self.state = 66
                self.match(STLParser.COMMA)
                self.state = 67
                self.match(STLParser.INF)
                self.state = 68
                self.match(STLParser.RBRAT)
                pass

            elif la_ == 3:
                localctx = STLParser.EmptyTimeBoundsContext(self, localctx)
                self.enterOuterAlt(localctx, 3)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return STLParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(STLParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class NaturalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NATURAL(self):
            return self.getToken(STLParser.NATURAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNatural" ):
                listener.enterNatural(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNatural" ):
                listener.exitNatural(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNatural" ):
                return visitor.visitNatural(self)
            else:
                return visitor.visitChildren(self)


    class NegNaturalContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(STLParser.MINUS, 0)
        def NATURAL(self):
            return self.getToken(STLParser.NATURAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegNatural" ):
                listener.enterNegNatural(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegNatural" ):
                listener.exitNegNatural(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegNatural" ):
                return visitor.visitNegNatural(self)
            else:
                return visitor.visitChildren(self)


    class NegNumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(STLParser.MINUS, 0)
        def NUMBER(self):
            return self.getToken(STLParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegNumber" ):
                listener.enterNegNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegNumber" ):
                listener.exitNegNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegNumber" ):
                return visitor.visitNegNumber(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = STLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr)
        try:
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = STLParser.NumberContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.match(STLParser.NUMBER)
                pass

            elif la_ == 2:
                localctx = STLParser.NegNumberContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.match(STLParser.MINUS)
                self.state = 75
                self.match(STLParser.NUMBER)
                pass

            elif la_ == 3:
                localctx = STLParser.NaturalContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.match(STLParser.NATURAL)
                pass

            elif la_ == 4:
                localctx = STLParser.NegNaturalContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 77
                self.match(STLParser.MINUS)
                self.state = 78
                self.match(STLParser.NATURAL)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





