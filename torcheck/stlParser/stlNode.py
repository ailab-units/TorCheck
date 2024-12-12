from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream

from torcheck.stl import Until, Atom, Eventually, Globally, And, Or, Not
from torcheck.stlParser.STLLexer import STLLexer
from torcheck.stlParser.STLParser import STLParser
from torcheck.stlParser.STLVisitor import STLVisitor


class stlNode(STLVisitor):

    def visitTextFormula(self, ctx: STLParser.TextFormulaContext):
        return self.visit(ctx.formula())

    def visitParensFormula(self, ctx:STLParser.ParensFormulaContext):
        return self.visit(ctx.formula())

    def visitU(self, ctx: STLParser.UContext):
        interval = self.visit(ctx.interval())
        left_formula = self.visit(ctx.formula(0))
        right_formula = self.visit(ctx.formula(1))
        if interval is None:
            return Until(left_formula, right_formula, unbound=True)
        elif interval[1] is None:
            return Until(left_formula, right_formula, left_time_bound=interval[0], right_unbound=True)
        return Until(left_formula, right_formula, left_time_bound=interval[0], right_time_bound=interval[1])

    def visitF(self, ctx: STLParser.FContext):
        interval = self.visit(ctx.interval())
        child = self.visit(ctx.formula())
        if interval is None:
            return Eventually(child, unbound=True)
        elif interval[1] is None:
            return Eventually(child, left_time_bound=interval[0], right_unbound=True)
        return Eventually(child, left_time_bound=interval[0], right_time_bound=interval[1])

    def visitG(self, ctx: STLParser.GContext):
        interval = self.visit(ctx.interval())
        child = self.visit(ctx.formula())
        if interval is None:
            return Globally(child, unbound=True)
        elif interval[1] is None:
            return Globally(child, left_time_bound=interval[0], right_unbound=True)
        return Globally(child, left_time_bound=interval[0], right_time_bound=interval[1])

    def visitAndOr(self, ctx:STLParser.AndOrContext):
        left_formula = self.visit(ctx.formula(0))
        right_formula = self.visit(ctx.formula(1))
        if ctx.op.text.strip() == 'and':
            return And(left_formula, right_formula)
        return Or(left_formula, right_formula)

    def visitNot(self, ctx: STLParser.NotContext):
        child = self.visit(ctx.formula())
        return Not(child)

    def visitAtom(self, ctx: STLParser.AtomContext):
        var_idx = self.visit(ctx.var())
        var_thresh = self.visit(ctx.expr())
        atom_lte = (ctx.op.text == '<=')
        return Atom(var_index=var_idx, threshold=var_thresh, lte=atom_lte)

    def visitNumber(self, ctx: STLParser.NumberContext):
        return float(ctx.NUMBER().getText())

    def visitNegNumber(self, ctx:STLParser.NegNumberContext):
        return -float(ctx.NUMBER().getText())

    def visitNatural(self, ctx: STLParser.NaturalContext):
        return int(ctx.NATURAL().getText())

    def visitNegNatural(self, ctx:STLParser.NegNaturalContext):
        return -int(ctx.NATURAL().getText())

    def visitTimeBounds(self, ctx: STLParser.TimeBoundsContext):
        t0 = self.visit(ctx.expr(0))
        t1 = self.visit(ctx.expr(1))
        return t0, t1

    def visitRightUnbound(self, ctx:STLParser.RightUnboundContext):
        t0 = self.visit(ctx.expr())
        return t0, None

    def visitEmptyTimeBounds(self, ctx: STLParser.EmptyTimeBoundsContext):
        return None

    def visitAtomicPredicate(self, ctx: STLParser.AtomicPredicateContext):
        return int(ctx.NATURAL().getText())


def from_string_to_formula(str_formula):
    expr = InputStream(str_formula + '\n')
    lexer = STLLexer(input=expr)
    token_stream = CommonTokenStream(lexer)
    parser = STLParser(token_stream)
    tree = parser.prog()
    visitor = stlNode()
    return visitor.visit(tree)
