from __future__ import annotations
from typing import Type

from ..qval import QOpt, QVar, IQOpt

from ..sugar import type_check
from ..env import Expr, Env, expr_type_check

import numpy as np


class EIQOpt(Expr):
    '''
    The Expression of Indexed Quantum Operators.
    
    EIQOpt ::= EQOpt EQVar

    Nonterminal.
    '''

    def __init__(self, qopt : Expr, qvar : Expr, env : Env):
        super().__init__(env)

        expr_type_check(qopt, QOpt)
        self._qopt = qopt

        expr_type_check(qvar, QVar)
        self._qvar = qvar


    ##################################
    # Expression settings

    @property
    def T(self) -> Type:
        return IQOpt
    
    def eval(self) -> object:
        return IQOpt(self._qopt.eval(), self._qvar.eval())    # type: ignore
    
    def __str__(self) -> str:
        return str(self._qopt) + str(self._qvar)
    ##################################

    
class EIQOptAdd(Expr):
    '''
    The Expression for additions of Indexed Quantum Operators.
    
    EIQOptAdd ::= (a : IQOpt) '+' (b : IQOpt)

    Nonterminal.
    '''

    def __init__(self, ioptA : Expr, ioptB : Expr, env : Env):
        super().__init__(env)

        type_check(ioptA, Expr)
        expr_type_check(ioptA, IQOpt)
        self._ioptA = ioptA

        type_check(ioptB, Expr)
        expr_type_check(ioptB, IQOpt)
        self._ioptB = ioptB


    ##################################
    # Expression settings

    @property
    def T(self) -> Type:
        return IQOpt
    
    def eval(self) -> object:
        return self._ioptA.eval() + self._ioptB.eval()  # type: ignore
    
    def __str__(self) -> str:
        return "(" + str(self._ioptA) + "+" + str(self._ioptB) + ")"
    ##################################


class EIQOptNeg(Expr):
    '''
    The expression for negation of an indexed quantum operator.

    EIQOptNeg ::= '(' '-' (a : IQOpt) ')'
    
    Nonterminal.
    '''

    def __init__(self, iopt : Expr, env : Env):
        super().__init__(env)

        type_check(iopt, Expr)
        expr_type_check(iopt, IQOpt)
        self._iopt = iopt

    ##################################
    # Expression settings

    @property
    def T(self) -> Type:
        return IQOpt
    
    def eval(self) -> object:
        return -self._iopt.eval()    # type: ignore
    
    def __str__(self) -> str:
        return "(-" + str(self._iopt) + ")"
    
    ##################################

class EIQOptSub(Expr):
    '''
    The Expression for subtraction of Indexed Quantum Operators.
    
    EIQOptSub ::= (a : IQOpt) '-' (b : IQOpt)

    Nonterminal.
    '''

    def __init__(self, ioptA : Expr, ioptB : Expr, env : Env):
        super().__init__(env)

        type_check(ioptA, Expr)
        expr_type_check(ioptA, IQOpt)
        self._ioptA = ioptA

        type_check(ioptB, Expr)
        expr_type_check(ioptB, IQOpt)
        self._ioptB = ioptB


    ##################################
    # Expression settings

    @property
    def T(self) -> Type:
        return IQOpt
    
    def eval(self) -> object:
        return self._ioptA.eval() - self._ioptB.eval()  # type: ignore
    
    def __str__(self) -> str:
        return "(" + str(self._ioptA) + "-" + str(self._ioptB) + ")"
    ##################################


class EIQOptScale(Expr):
    '''
    The expression for scaling of quantum operators.

    EIQOptScale ::= (c : complex) (b : IQOpt)
                | (c : complex) '*' (b : IQOpt)
    
    Nonterminal.
    '''

    def __init__(self, c : complex, iopt : Expr, env : Env):
        super().__init__(env)

        type_check(c, (complex, float))
        self._c = c

        type_check(iopt, Expr)
        expr_type_check(iopt, QOpt)
        self._iopt = iopt

    ##################################
    # Expression settings

    @property
    def T(self) -> Type:
        return IQOpt
    
    def eval(self) -> object:
        return self._c * self._iopt.eval() # type: ignore
    
    def __str__(self) -> str:
        return "(" + str(self._c) + " " + str(self._iopt) + ")"
    
    ##################################


class EIQOptMul(Expr):
    '''
    The Expression for multiplications of Indexed Quantum Operators.
    
    EIQOptMul ::= (a : IQOpt) (b : IQOpt)
                | (a : IQOpt) '*' (b : IQOpt)

    Nonterminal.
    '''

    def __init__(self, ioptA : Expr, ioptB : Expr, env : Env):
        super().__init__(env)

        type_check(ioptA, Expr)
        expr_type_check(ioptA, IQOpt)
        self._ioptA = ioptA

        type_check(ioptB, Expr)
        expr_type_check(ioptB, IQOpt)
        self._ioptB = ioptB


    ##################################
    # Expression settings

    @property
    def T(self) -> Type:
        return IQOpt
    
    def eval(self) -> object:
        return self._ioptA.eval() @ self._ioptB.eval()  # type: ignore
    
    def __str__(self) -> str:
        return "(" + str(self._ioptA) + " " + str(self._ioptB) + ")"
    ##################################


class EIQOptDagger(Expr):
    '''
    The expression for the conjugate transpose of an indexed quantum operator.

    EIQOptDagger ::= (a : IQOpt) '^\\dagger'
                    | (a : IQOpt) '†'
    
    Nonterminal.
    '''

    def __init__(self, iopt : Expr, env : Env):
        super().__init__(env)

        type_check(iopt, Expr)
        expr_type_check(iopt, IQOpt)
        self._iopt = iopt

    ##################################
    # Expression settings

    @property
    def T(self) -> Type:
        return IQOpt
    
    def eval(self) -> object:
        return self._iopt.eval().dagger()    # type: ignore
    
    def __str__(self) -> str:
        return "(" + str(self._iopt) + "†" + ")"
    
    ##################################


class EIQOptTensor(Expr):
    '''
    The expression for tensor product of indexed quantum operators.

    EIQOptTensor ::= (a : IQOpt) '⊗' (b : IQOpt)
                    | (a : IQOpt) '\\otimes' (b : IQOpt)
    
    Nonterminal.
    '''

    def __init__(self, ioptA : Expr, ioptB : Expr, env : Env):
        super().__init__(env)

        type_check(ioptA, Expr)
        expr_type_check(ioptA, IQOpt)
        self._ioptA = ioptA

        type_check(ioptB, Expr)
        expr_type_check(ioptB, IQOpt)
        self._ioptB = ioptB

    ##################################
    # Expression settings

    @property
    def T(self) -> Type:
        return IQOpt
    
    def eval(self) -> object:
        return self._ioptA.eval().tensor(self._ioptB.eval())    # type: ignore
    
    def __str__(self) -> str:
        return "(" + str(self._ioptA) + "⊗" + str(self._ioptB) + ")"
    
    ##################################



class EIQOptDisjunct(Expr):
    '''
    The expression for disjunction of projective indexed quantum operators.

    EIQOptDisjunct ::= (a : IQOpt) '\\vee' (b : IQOpt)
                    | (a : IQOpt) '∨' (b : IQOpt)
    
    Nonterminal.
    '''

    def __init__(self, ioptA : Expr, ioptB : Expr, env : Env):
        super().__init__(env)

        type_check(ioptA, Expr)
        expr_type_check(ioptA, IQOpt)
        self._ioptA = ioptA

        type_check(ioptB, Expr)
        expr_type_check(ioptB, IQOpt)
        self._ioptB = ioptB

    ##################################
    # Expression settings

    @property
    def T(self) -> Type:
        return IQOpt
    
    def eval(self) -> object:
        return self._ioptA.eval() | self._ioptB.eval()    # type: ignore
    
    def __str__(self) -> str:
        return "(" + str(self._ioptA) + " ∨ " + str(self._ioptB) + ")"
    
    ##################################

class EIQOptConjunct(Expr):
    '''
    The expression for conjunction of projective indexed quantum operators.

    EIQOptConjunct   ::= (a : IQOpt) '\\wedge' (b : IQOpt)
                    | (a : IQOpt) '∧' (b : IQOpt)
    
    Nonterminal.
    '''

    def __init__(self, ioptA : Expr, ioptB : Expr, env : Env):
        super().__init__(env)

        type_check(ioptA, Expr)
        expr_type_check(ioptA, IQOpt)
        self._ioptA = ioptA

        type_check(ioptB, Expr)
        expr_type_check(ioptB, IQOpt)
        self._ioptB = ioptB

    ##################################
    # Expression settings

    @property
    def T(self) -> Type:
        return IQOpt
    
    def eval(self) -> object:
        return self._ioptA.eval() & self._ioptB.eval()    # type: ignore
    
    def __str__(self) -> str:
        return "(" + str(self._ioptA) + " ∧ " + str(self._ioptB) + ")"
    
    ##################################


class EIQOptComplement(Expr):
    '''
    The expression for complement of projective quantum operators.

    EIQOptComplement ::= (a : IQOpt) '^\\bot'
                    | (a : IQOpt) '^⊥'
    
    Nonterminal.
    '''

    def __init__(self, iopt : Expr, env : Env):
        super().__init__(env)

        type_check(iopt, Expr)
        expr_type_check(iopt, IQOpt)
        self._iopt = iopt


    ##################################
    # Expression settings

    @property
    def T(self) -> Type:
        return IQOpt
    
    def eval(self) -> object:
        return (~ self._iopt.eval())    # type: ignore
    
    def __str__(self) -> str:
        return "(" + str(self._iopt) + "^⊥)"
    
    ##################################


class EIQOptSasakiImply(Expr):
    '''
    The expression for Sasaki implication of projective quantum operators.

    EIQOptSasakiImply   ::= (a : IQOpt) '\\SasakiImply' (b : IQOpt)
                        | (a : IQOpt) '⇝' (b : IQOpt)
    
    Nonterminal.
    '''

    def __init__(self, ioptA : Expr, ioptB : Expr, env : Env):
        super().__init__(env)

        type_check(ioptA, Expr)
        expr_type_check(ioptA, IQOpt)
        self._ioptA = ioptA

        type_check(ioptB, Expr)
        expr_type_check(ioptB, IQOpt)
        self._ioptB = ioptB

    ##################################
    # Expression settings

    @property
    def T(self) -> Type:
        return IQOpt
    
    def eval(self) -> object:
        return self._ioptA.eval().Sasaki_imply(self._ioptB.eval())    # type: ignore
    
    def __str__(self) -> str:
        return "(" + str(self._ioptA) + " ⇝ " + str(self._ioptB) + ")"
    
    ##################################

class EIQOptSasakiConjunct(Expr):
    '''
    The expression for Sasaki conjunction of projective quantum operators.

    EIQOptSasakiConjunct ::= (a : IQOpt) '\\SasakiConjunct' (b : IQOpt)
                        | (a : IQOpt) '⋒' (b : IQOpt)
    
    Nonterminal.
    '''

    def __init__(self, ioptA : Expr, ioptB : Expr, env : Env):
        super().__init__(env)

        type_check(ioptA, Expr)
        expr_type_check(ioptA, IQOpt)
        self._ioptA = ioptA

        type_check(ioptB, Expr)
        expr_type_check(ioptB, IQOpt)
        self._ioptB = ioptB

    ##################################
    # Expression settings

    @property
    def T(self) -> Type:
        return IQOpt
    
    def eval(self) -> object:
        return self._ioptA.eval().Sasaki_conjunct(self._ioptB.eval())    # type: ignore
    
    def __str__(self) -> str:
        return "(" + str(self._ioptA) + " ⋒ " + str(self._ioptB) + ")"
    
    ##################################