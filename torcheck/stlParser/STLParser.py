# Generated from STL.g4 by ANTLR 4.13.2
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
        4,1,31,100,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,4,0,12,8,
        0,11,0,12,0,13,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,70,8,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,3,3,81,8,3,1,3,1,3,1,3,5,3,86,8,3,10,3,12,
        3,89,9,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,98,8,4,1,4,0,1,6,5,0,2,
        4,6,8,0,5,1,0,17,18,1,0,22,26,1,0,11,12,1,0,1,2,1,0,13,16,109,0,
        11,1,0,0,0,2,24,1,0,0,0,4,69,1,0,0,0,6,80,1,0,0,0,8,97,1,0,0,0,10,
        12,3,2,1,0,11,10,1,0,0,0,12,13,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,
        0,14,1,1,0,0,0,15,16,3,4,2,0,16,17,5,29,0,0,17,25,1,0,0,0,18,19,
        5,1,0,0,19,20,5,20,0,0,20,21,3,6,3,0,21,22,5,29,0,0,22,25,1,0,0,
        0,23,25,5,29,0,0,24,15,1,0,0,0,24,18,1,0,0,0,24,23,1,0,0,0,25,3,
        1,0,0,0,26,27,5,3,0,0,27,28,3,4,2,0,28,29,5,4,0,0,29,30,7,0,0,0,
        30,31,5,3,0,0,31,32,3,4,2,0,32,33,5,4,0,0,33,70,1,0,0,0,34,35,5,
        19,0,0,35,36,5,3,0,0,36,37,3,4,2,0,37,38,5,4,0,0,38,70,1,0,0,0,39,
        40,3,6,3,0,40,41,7,1,0,0,41,42,3,6,3,0,42,70,1,0,0,0,43,44,5,3,0,
        0,44,45,3,4,2,0,45,46,5,4,0,0,46,70,1,0,0,0,47,70,7,2,0,0,48,49,
        5,3,0,0,49,50,3,4,2,0,50,51,5,4,0,0,51,52,5,8,0,0,52,53,3,8,4,0,
        53,54,5,3,0,0,54,55,3,4,2,0,55,56,5,4,0,0,56,70,1,0,0,0,57,58,5,
        9,0,0,58,59,3,8,4,0,59,60,5,3,0,0,60,61,3,4,2,0,61,62,5,4,0,0,62,
        70,1,0,0,0,63,64,5,10,0,0,64,65,3,8,4,0,65,66,5,3,0,0,66,67,3,4,
        2,0,67,68,5,4,0,0,68,70,1,0,0,0,69,26,1,0,0,0,69,34,1,0,0,0,69,39,
        1,0,0,0,69,43,1,0,0,0,69,47,1,0,0,0,69,48,1,0,0,0,69,57,1,0,0,0,
        69,63,1,0,0,0,70,5,1,0,0,0,71,72,6,3,-1,0,72,81,5,27,0,0,73,74,5,
        14,0,0,74,81,5,27,0,0,75,81,7,3,0,0,76,77,5,3,0,0,77,78,3,6,3,0,
        78,79,5,4,0,0,79,81,1,0,0,0,80,71,1,0,0,0,80,73,1,0,0,0,80,75,1,
        0,0,0,80,76,1,0,0,0,81,87,1,0,0,0,82,83,10,5,0,0,83,84,7,4,0,0,84,
        86,3,6,3,6,85,82,1,0,0,0,86,89,1,0,0,0,87,85,1,0,0,0,87,88,1,0,0,
        0,88,7,1,0,0,0,89,87,1,0,0,0,90,91,5,6,0,0,91,92,3,6,3,0,92,93,5,
        5,0,0,93,94,3,6,3,0,94,95,5,7,0,0,95,98,1,0,0,0,96,98,1,0,0,0,97,
        90,1,0,0,0,97,96,1,0,0,0,98,9,1,0,0,0,6,13,24,69,80,87,97
    ]

class STLParser ( Parser ):

    grammarFileName = "STL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'('", "')'", 
                     "','", "'['", "']'", "'U_'", "'F_'", "'G_'", "'True'", 
                     "'False'", "'+'", "'-'", "'*'", "'/'", "'&'", "'|'", 
                     "'!'", "'='", "'!='", "'>'", "'>='", "'<'", "'<='", 
                     "'=='" ]

    symbolicNames = [ "<INVALID>", "PARAMETERS", "SERIES", "LPAR", "RPAR", 
                      "COMMA", "LBRAT", "RBRAT", "U", "F", "G", "TRUE", 
                      "FALSE", "PLUS", "MINUS", "MULT", "DIV", "AND", "OR", 
                      "NOT", "EQ", "NEQ", "GT", "GE", "LT", "LE", "E", "NUMBER", 
                      "ID", "NEWLINE", "COMMENT", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_formula = 2
    RULE_expr = 3
    RULE_interval = 4

    ruleNames =  [ "prog", "stat", "formula", "expr", "interval" ]

    EOF = Token.EOF
    PARAMETERS=1
    SERIES=2
    LPAR=3
    RPAR=4
    COMMA=5
    LBRAT=6
    RBRAT=7
    U=8
    F=9
    G=10
    TRUE=11
    FALSE=12
    PLUS=13
    MINUS=14
    MULT=15
    DIV=16
    AND=17
    OR=18
    NOT=19
    EQ=20
    NEQ=21
    GT=22
    GE=23
    LT=24
    LE=25
    E=26
    NUMBER=27
    ID=28
    NEWLINE=29
    COMMENT=30
    WS=31

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STLParser.StatContext)
            else:
                return self.getTypedRuleContext(STLParser.StatContext,i)


        def getRuleIndex(self):
            return STLParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = STLParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.stat()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 671637006) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return STLParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.StatContext
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


    class TextformulaContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(STLParser.FormulaContext,0)

        def NEWLINE(self):
            return self.getToken(STLParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTextformula" ):
                listener.enterTextformula(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTextformula" ):
                listener.exitTextformula(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTextformula" ):
                return visitor.visitTextformula(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PARAMETERS(self):
            return self.getToken(STLParser.PARAMETERS, 0)
        def EQ(self):
            return self.getToken(STLParser.EQ, 0)
        def expr(self):
            return self.getTypedRuleContext(STLParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(STLParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = STLParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = STLParser.TextformulaContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.formula()
                self.state = 16
                self.match(STLParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = STLParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.match(STLParser.PARAMETERS)
                self.state = 19
                self.match(STLParser.EQ)
                self.state = 20
                self.expr(0)
                self.state = 21
                self.match(STLParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = STLParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 23
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
        def LPAR(self):
            return self.getToken(STLParser.LPAR, 0)
        def formula(self):
            return self.getTypedRuleContext(STLParser.FormulaContext,0)

        def RPAR(self):
            return self.getToken(STLParser.RPAR, 0)

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

        def LPAR(self, i:int=None):
            if i is None:
                return self.getTokens(STLParser.LPAR)
            else:
                return self.getToken(STLParser.LPAR, i)
        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STLParser.FormulaContext)
            else:
                return self.getTypedRuleContext(STLParser.FormulaContext,i)

        def RPAR(self, i:int=None):
            if i is None:
                return self.getTokens(STLParser.RPAR)
            else:
                return self.getToken(STLParser.RPAR, i)
        def U(self):
            return self.getToken(STLParser.U, 0)
        def interval(self):
            return self.getTypedRuleContext(STLParser.IntervalContext,0)


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


    class TrueFalseContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.FormulaContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(STLParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(STLParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrueFalse" ):
                listener.enterTrueFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrueFalse" ):
                listener.exitTrueFalse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrueFalse" ):
                return visitor.visitTrueFalse(self)
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

        def LPAR(self, i:int=None):
            if i is None:
                return self.getTokens(STLParser.LPAR)
            else:
                return self.getToken(STLParser.LPAR, i)
        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STLParser.FormulaContext)
            else:
                return self.getTypedRuleContext(STLParser.FormulaContext,i)

        def RPAR(self, i:int=None):
            if i is None:
                return self.getTokens(STLParser.RPAR)
            else:
                return self.getToken(STLParser.RPAR, i)
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

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STLParser.ExprContext)
            else:
                return self.getTypedRuleContext(STLParser.ExprContext,i)

        def GT(self):
            return self.getToken(STLParser.GT, 0)
        def GE(self):
            return self.getToken(STLParser.GE, 0)
        def LT(self):
            return self.getToken(STLParser.LT, 0)
        def LE(self):
            return self.getToken(STLParser.LE, 0)
        def E(self):
            return self.getToken(STLParser.E, 0)

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
        self.enterRule(localctx, 4, self.RULE_formula)
        self._la = 0 # Token type
        try:
            self.state = 69
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = STLParser.AndOrContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.match(STLParser.LPAR)
                self.state = 27
                self.formula()
                self.state = 28
                self.match(STLParser.RPAR)
                self.state = 29
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 30
                self.match(STLParser.LPAR)
                self.state = 31
                self.formula()
                self.state = 32
                self.match(STLParser.RPAR)
                pass

            elif la_ == 2:
                localctx = STLParser.NotContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(STLParser.NOT)
                self.state = 35
                self.match(STLParser.LPAR)
                self.state = 36
                self.formula()
                self.state = 37
                self.match(STLParser.RPAR)
                pass

            elif la_ == 3:
                localctx = STLParser.AtomContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.expr(0)
                self.state = 40
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 130023424) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 41
                self.expr(0)
                pass

            elif la_ == 4:
                localctx = STLParser.ParensFormulaContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 43
                self.match(STLParser.LPAR)
                self.state = 44
                self.formula()
                self.state = 45
                self.match(STLParser.RPAR)
                pass

            elif la_ == 5:
                localctx = STLParser.TrueFalseContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 47
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==11 or _la==12):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 6:
                localctx = STLParser.UContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 48
                self.match(STLParser.LPAR)
                self.state = 49
                self.formula()
                self.state = 50
                self.match(STLParser.RPAR)
                self.state = 51
                self.match(STLParser.U)
                self.state = 52
                self.interval()
                self.state = 53
                self.match(STLParser.LPAR)
                self.state = 54
                self.formula()
                self.state = 55
                self.match(STLParser.RPAR)
                pass

            elif la_ == 7:
                localctx = STLParser.FContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 57
                self.match(STLParser.F)
                self.state = 58
                self.interval()
                self.state = 59
                self.match(STLParser.LPAR)
                self.state = 60
                self.formula()
                self.state = 61
                self.match(STLParser.RPAR)
                pass

            elif la_ == 8:
                localctx = STLParser.GContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 63
                self.match(STLParser.G)
                self.state = 64
                self.interval()
                self.state = 65
                self.match(STLParser.LPAR)
                self.state = 66
                self.formula()
                self.state = 67
                self.match(STLParser.RPAR)
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


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def PARAMETERS(self):
            return self.getToken(STLParser.PARAMETERS, 0)
        def SERIES(self):
            return self.getToken(STLParser.SERIES, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class ParensExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(STLParser.LPAR, 0)
        def expr(self):
            return self.getTypedRuleContext(STLParser.ExprContext,0)

        def RPAR(self):
            return self.getToken(STLParser.RPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParensExpr" ):
                listener.enterParensExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParensExpr" ):
                listener.exitParensExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParensExpr" ):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)


    class AlgOpContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a STLParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(STLParser.ExprContext)
            else:
                return self.getTypedRuleContext(STLParser.ExprContext,i)

        def MULT(self):
            return self.getToken(STLParser.MULT, 0)
        def DIV(self):
            return self.getToken(STLParser.DIV, 0)
        def PLUS(self):
            return self.getToken(STLParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(STLParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlgOp" ):
                listener.enterAlgOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlgOp" ):
                listener.exitAlgOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlgOp" ):
                return visitor.visitAlgOp(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = STLParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                localctx = STLParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 72
                self.match(STLParser.NUMBER)
                pass
            elif token in [14]:
                localctx = STLParser.NegNumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 73
                self.match(STLParser.MINUS)
                self.state = 74
                self.match(STLParser.NUMBER)
                pass
            elif token in [1, 2]:
                localctx = STLParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 75
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [3]:
                localctx = STLParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 76
                self.match(STLParser.LPAR)
                self.state = 77
                self.expr(0)
                self.state = 78
                self.match(STLParser.RPAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = STLParser.AlgOpContext(self, STLParser.ExprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 82
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 83
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 84
                    self.expr(6) 
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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



    def interval(self):

        localctx = STLParser.IntervalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_interval)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                localctx = STLParser.TimeBoundsContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.match(STLParser.LBRAT)
                self.state = 91
                self.expr(0)
                self.state = 92
                self.match(STLParser.COMMA)
                self.state = 93
                self.expr(0)
                self.state = 94
                self.match(STLParser.RBRAT)
                pass
            elif token in [3]:
                localctx = STLParser.EmptyTimeBoundsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         




