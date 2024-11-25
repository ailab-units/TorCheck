from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream

from torcheck.stl import Until,Atom
from torcheck.stlParser.STLLexer import STLLexer
from torcheck.stlParser.STLParser import STLParser
from torcheck.stlParser.STLVisitor import STLVisitor


class stlNode(STLVisitor):

    def visitU(self, ctx: STLParser.UContext):
        interval = self.visit(ctx.interval())
        left_formula = self.visit(ctx.formula(0))
        right_formula = self.visitF(ctx.formula(1))
        if interval is None:
            return Until(left_formula, right_formula, unbound=True)
        return Until(left_formula, right_formula, left_time_bound=interval[0], right_time_bound=interval[1])

    def visitNumber(self, ctx: STLParser.NumberContext):
        return float(ctx.NUMBER().getText())

    def visitTimeBounds(self, ctx: STLParser.TimeBoundsContext):
        t0 = self.visit(ctx.expr(0))
        t1 = self.visit(ctx.expr(1))
        return t0, t1

    def visitEmptyTimeBounds(self, ctx: STLParser.EmptyTimeBoundsContext):
        return None

    def visitAlgOp(self, ctx: STLParser.AlgOpContext):
        super().visitAlgOp(ctx)

    def visitAtom(self, ctx: STLParser.AtomContext):
       return Atom()


formula = "((X>0)U_(Y>2))"
expr = InputStream(formula + '\n')
lexer = STLLexer(input=expr)
token_stream = CommonTokenStream(lexer)
parser = STLParser(token_stream)
a = stlNode().visit(parser.prog())
print(a)
