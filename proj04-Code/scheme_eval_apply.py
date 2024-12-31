import sys
import os

from pair import *
from scheme_utils import *
from ucb import main, trace

import scheme_forms

##############
# Eval/Apply #
##############


def scheme_eval(expr, env, _=None):  # Optional third argument is ignored
    """Evaluate Scheme expression EXPR in Frame ENV.

    >>> expr = read_line('(+ 2 2)')
    >>> expr
    Pair('+', Pair(2, Pair(2, nil)))
    >>> scheme_eval(expr, create_global_frame())
    4
    """
    # Evaluate atoms
    if scheme_symbolp(expr):
        return env.lookup(expr)
    elif self_evaluating(expr):
        return expr

    # All non-atomic expressions are lists (combinations)
    if not scheme_listp(expr):
        raise SchemeError('malformed list: {0}'.format(repl_str(expr)))
    first, rest = expr.first, expr.rest
    if scheme_symbolp(first) and first in scheme_forms.SPECIAL_FORMS:
        return scheme_forms.SPECIAL_FORMS[first](rest, env)
    else:
        # BEGIN PROBLEM 3
        operator = scheme_eval(first, env)
        if not isinstance(operator, Procedure):
            raise SchemeError('operator is not a procedure: {0}'.format(repl_str(operator)))
        operands = rest.map(lambda operand: scheme_eval(operand, env))
        return scheme_apply(operator, operands, env)
   

        # END PROBLEM 3


def scheme_apply(procedure, args, env):
    """Apply Scheme PROCEDURE to argument values ARGS (a Scheme list) in
    Frame ENV, the current environment."""
    validate_procedure(procedure)
    if isinstance(procedure, BuiltinProcedure):
        # BEGIN PROBLEM 2
        arg_list=[]
        while(args != nil):
            arg_list.append(args.first)
            args=args.rest
        try:
            if procedure.expect_env:
                return procedure.py_func(*(arg_list+[env]))
            else:
                return procedure.py_func(*arg_list)
        except TypeError:
            raise SchemeError('incorrect number of arguments')
        # END PROBLEM 2
    elif isinstance(procedure, LambdaProcedure):
        # BEGIN PROBLEM 9
        child=procedure.env.make_child_frame(procedure.formals, args)
        return eval_all(procedure.body,child)
        # END PROBLEM 9
    elif isinstance(procedure, MuProcedure):
        # BEGIN PROBLEM 11
        child=env.make_child_frame(procedure.formals, args)
        return eval_all(procedure.body, child)
        # END PROBLEM 11
    else:
        assert False, "Unexpected procedure: {}".format(procedure)


def eval_all(expressions, env):
    """Evaluate each expression in the Scheme list EXPRESSIONS in
    Frame ENV (the current environment) and return the value of the last.

    >>> eval_all(read_line("(1)"), create_global_frame())
    1
    >>> eval_all(read_line("(1 2)"), create_global_frame())
    2
    >>> x = eval_all(read_line("((print 1) 2)"), create_global_frame())
    1
    >>> x
    2
    >>> eval_all(read_line("((define x 2) x)"), create_global_frame())
    2
    """
    # BEGIN PROBLEM 6
    if (expressions is nil):
        return None
    else:
        while expressions.rest is not nil:
            scheme_eval(expressions.first,env)
            expressions=expressions.rest
        re=scheme_eval(expressions.first, env, True)
        return re
    # END PROBLEM 6


##################
# Tail Recursion #
##################

class Unevaluated:
    """An expression and an environment in which it is to be evaluated."""

    def __init__(self, expr, env):
        """Expression EXPR to be evaluated in Frame ENV."""
        self.expr = expr
        self.env = env
    def __str__(self):
        return str(self.expr)


def optimize_tail_calls(original_scheme_eval):
    """Return a properly tail recursive version of an eval function."""
    """
    Complete the function optimize_tail_calls in scheme_eval_apply.py. It returns an alternative to scheme_eval that is properly tail recursive. That is, the interpreter will allow an unbounded number of active tail calls in constant space. It has a third argument tail that indicates whether the expression to be evaluated is in a tail context.

The Unevaluated class represents an expression that needs to be evaluated in an environment. When optimized_eval receives a non-atomic expression in a tail context, it returns an Unevaluated instance. Otherwise, it should repeatedly call original_scheme_eval until the result is a value, rather than an Unevaluated.

A successful implementation will require changes to several other functions, including some functions that we provided for you. All expressions throughout your interpreter that are in a tail context should be evaluated by calling scheme_eval with True as the third argument (now called tail). Your goal is to determine which expressions are in a tail context throughout your code and change calls to scheme_eval as needed.
    """
    def optimized_eval(expr, env, tail=False):
        """Evaluate Scheme expression EXPR in Frame ENV. If TAIL,
        return an Unevaluated containing an expression for further evaluation.
        """
        if tail and not scheme_symbolp(expr) and not self_evaluating(expr):
            return Unevaluated(expr,env)
        # BEGIN PROBLEM EC


        res=original_scheme_eval(expr, env)

        while isinstance(res, Unevaluated):
            res = original_scheme_eval(res.expr, res.env)
        return res
        # END PROBLEM EC
    return optimized_eval


################################################################
# Uncomment the following line to apply tail call optimization #
################################################################
scheme_eval = optimize_tail_calls(scheme_eval)
