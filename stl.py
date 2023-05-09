#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==============================================================================
# Copyright 2020-* Luca Bortolussi. All Rights Reserved.
# Copyright 2020-* Laura Nenzi.     All Rights Reserved.
# Copyright 2020-* AILab @ UniTS.   All Rights Reserved.
# ==============================================================================

"""A fully-differentiable implementation of Signal Temporal Logic semantic trees."""

# For custom type-hints
from typing import TypeVar, Union

# For tensor functions
import torch
import torch.nn.functional as F
from torch import Tensor

# Custom types for method binding at typecheck
NodeType = TypeVar("NodeType", bound="Node")
AtomType = TypeVar("AtomType", bound="Atom")
EqualType = TypeVar("EqualType", bound="Equal")
NotType = TypeVar("NotType", bound="Not")
AndType = TypeVar("AndType", bound="And")
OrType = TypeVar("OrType", bound="Or")
GloballyType = TypeVar("GloballyType", bound="Globally")
EventuallyType = TypeVar("EventuallyType", bound="Eventually")


def eventually(x: Tensor, time_span: Union[float, int]) -> Tensor:
    """
    STL operator 'eventually' in 1D.

    Parameters
    ----------
    x: torch.Tensor
        Signal
    time_span: any numeric type
        Timespan duration

    Returns
    -------
    torch.Tensor
    A tensor containing the result of the operation.
    """
    return F.max_pool1d(x, kernel_size=time_span, stride=1)


class Node:
    """Abstract node class for STL semantics tree."""

    def __init__(self: NodeType) -> None:
        # Must be overloaded.
        pass

    def __str__(self: NodeType) -> str:
        # Must be overloaded.
        pass

    def boolean(
        self: NodeType, x: Tensor, evaluate_at_all_times: bool = False
    ) -> Tensor:
        """
        Evaluates the boolean semantics at the node.

        Parameters
        ----------
        x : torch.Tensor, of size N_samples x N_vars x N_sampling_points
            The input signals, stored as a batch tensor with trhee dimensions.
        evaluate_at_all_times: bool
            Whether to evaluate the semantics at all times (True) or
            just at t=0 (False).

        Returns
        -------
        torch.Tensor
        A tensor with the boolean semantics for the node.
        """
        z: Tensor = self._boolean(x)
        if evaluate_at_all_times:
            return z
        else:
            return self._extract_semantics_at_time_zero(z)

    def quantitative(
        self: NodeType,
        x: Tensor,
        normalize: bool = False,
        evaluate_at_all_times: bool = False,
    ) -> Tensor:
        """
        Evaluates the quantitative semantics at the node.

        Parameters
        ----------
        x : torch.Tensor, of size N_samples x N_vars x N_sampling_points
            The input signals, stored as a batch tensor with three dimensions.
        normalize: bool
            Whether the measure of robustness if normalized (True) or
            not (False). Currently not in use.
        evaluate_at_all_times: bool
            Whether to evaluate the semantics at all times (True) or
            just at t=0 (False).

        Returns
        -------
        torch.Tensor
        A tensor with the quantitative semantics for the node.
        """
        z: Tensor = self._quantitative(x, normalize)
        if evaluate_at_all_times:
            return z
        else:
            return self._extract_semantics_at_time_zero(z)

    def set_normalizing_flag(self: NodeType, value: bool = True) -> None:
        """
        Setter for the 'normalization of robustness of the formula' flag.
        Currently not in use.
        """

    def time_depth(self: NodeType) -> Union[float, int]:
        """Returns time depth of bounded temporal operators only."""
        # Must be overloaded.

    def _quantitative(self: NodeType, x: Tensor, normalize: bool = False) -> Tensor:
        """Private method equivalent to public one for inner call."""
        # Must be overloaded.

    def _boolean(self: NodeType, x: Tensor) -> Tensor:
        """Private method equivalent to public one for inner call."""
        # Must be overloaded.

    @staticmethod
    def _extract_semantics_at_time_zero(x: Tensor) -> Tensor:
        """Extrapolates the vector of truth values at time zero"""
        return torch.reshape(x[:, 0, 0], (-1,))


class Atom(Node):
    """Atomic formula node; for now of the form X<=t or X>=t"""

    def __init__(
        self: AtomType, var_index: int, threshold: Union[float, int], lte: bool = False
    ) -> None:
        super().__init__()
        self.var_index: int = var_index
        self.threshold: Union[float, int] = threshold
        self.lte: bool = lte

    def __str__(self: AtomType) -> str:
        s: str = (
            "x_"
            + str(self.var_index)
            + (" <= " if self.lte else " >= ")
            + str(self.threshold)
        )
        return s

    def time_depth(self: AtomType) -> Union[float, int]:
        return 0

    def _boolean(self: AtomType, x: Tensor) -> Tensor:
        # extract tensor of the same dimension as data, but with only one variable
        xj: Tensor = x[:, self.var_index, :]
        xj: Tensor = xj.view(xj.size()[0], 1, -1)
        if self.lte:
            z: Tensor = torch.le(xj, self.threshold)
        else:
            z: Tensor = torch.ge(xj, self.threshold)
        return z

    def _quantitative(self: AtomType, x: Tensor, normalize: bool = False) -> Tensor:
        # extract tensor of the same dimension as data, but with only one variable
        xj: Tensor = x[:, self.var_index, :]
        xj: Tensor = xj.view(xj.size()[0], 1, -1)
        if self.lte:
            z: Tensor = -xj + self.threshold
        else:
            z: Tensor = xj - self.threshold
        if normalize:
            z: Tensor = torch.tanh(z)
        return z


class Equal(Node):
    """Atomic formula node; for now of the form X==t"""

    def __init__(self: EqualType, var_index: int, rhs: Union[float, int]) -> None:
        super().__init__()
        self.var_index: int = var_index
        self.rhs: Union[float, int] = rhs

    def __str__(self: EqualType) -> str:
        s: str = "x_" + str(self.var_index) + (" ==") + str(self.rhs)
        return s

    def time_depth(self: EqualType) -> Union[float, int]:
        return 0

    def _boolean(self: EqualType, x: Tensor) -> Tensor:
        # extract tensor of the same dimension as data, but with only one variable
        xj: Tensor = x[:, self.var_index, :]
        xj: Tensor = xj.view(xj.size()[0], 1, -1)
        z: Tensor = torch.eq(xj, self.rhs)
        return z

    def _quantitative(self: EqualType, x: Tensor, normalize: bool = False) -> Tensor:
        # extract tensor of the same dimension as data, but with only one variable
        xj: Tensor = x[:, self.var_index, :]
        xj: Tensor = xj.view(xj.size()[0], 1, -1)
        z: Tensor = -torch.absolute(xj - self.rhs)
        if normalize:
            z: Tensor = torch.tanh(z)
        return z


class Not(Node):
    """Negation node."""

    def __init__(self: NotType, child: Node) -> None:
        super().__init__()
        self.child: Node = child

    def __str__(self: NotType) -> str:
        s: str = "not ( " + self.child.__str__() + " )"
        return s

    def time_depth(self: NotType) -> Union[float, int]:
        return self.child.time_depth()

    def _boolean(self: NotType, x: Tensor) -> Tensor:
        z: Tensor = ~self.child._boolean(x)
        return z

    def _quantitative(self: NotType, x: Tensor, normalize: bool = False) -> Tensor:
        z: Tensor = -self.child._quantitative(x, normalize)
        return z


class And(Node):
    """Conjunction node."""

    def __init__(self: AndType, left_child: Node, right_child: Node) -> None:
        super().__init__()
        self.left_child: Node = left_child
        self.right_child: Node = right_child

    def __str__(self: AndType) -> str:
        s: str = (
            "( "
            + self.left_child.__str__()
            + " and "
            + self.right_child.__str__()
            + " )"
        )
        return s

    def time_depth(self: AndType) -> Union[float, int]:
        return max(self.left_child.time_depth(), self.right_child.time_depth())

    def _boolean(self: AndType, x: Tensor) -> Tensor:
        z1: Tensor = self.left_child._boolean(x)
        z2: Tensor = self.right_child._boolean(x)
        size: int = min(z1.size()[2], z2.size()[2])
        z1: Tensor = z1[:, :, :size]
        z2: Tensor = z2[:, :, :size]
        z: Tensor = torch.logical_and(z1, z2)
        return z

    def _quantitative(self: AndType, x: Tensor, normalize: bool = False) -> Tensor:
        z1: Tensor = self.left_child._quantitative(x, normalize)
        z2: Tensor = self.right_child._quantitative(x, normalize)
        size: int = min(z1.size()[2], z2.size()[2])
        z1: Tensor = z1[:, :, :size]
        z2: Tensor = z2[:, :, :size]
        z: Tensor = torch.min(z1, z2)
        return z


class Or(Node):
    """Disjunction node."""

    def __init__(self: OrType, left_child: Node, right_child: Node) -> None:
        super().__init__()
        self.left_child: Node = left_child
        self.right_child: Node = right_child

    def __str__(self: OrType) -> str:
        s: str = (
            "( "
            + self.left_child.__str__()
            + " or "
            + self.right_child.__str__()
            + " )"
        )
        return s

    def time_depth(self: OrType) -> Union[float, int]:
        return max(self.left_child.time_depth(), self.right_child.time_depth())

    def _boolean(self: OrType, x: Tensor) -> Tensor:
        z1: Tensor = self.left_child._boolean(x)
        z2: Tensor = self.right_child._boolean(x)
        size: int = min(z1.size()[2], z2.size()[2])
        z1: Tensor = z1[:, :, :size]
        z2: Tensor = z2[:, :, :size]
        z: Tensor = torch.logical_or(z1, z2)
        return z

    def _quantitative(self: OrType, x: Tensor, normalize: bool = False) -> Tensor:
        z1: Tensor = self.left_child._quantitative(x, normalize)
        z2: Tensor = self.right_child._quantitative(x, normalize)
        size: int = min(z1.size()[2], z2.size()[2])
        z1: Tensor = z1[:, :, :size]
        z2: Tensor = z2[:, :, :size]
        z: Tensor = torch.max(z1, z2)
        return z


class Globally(Node):
    """Globally node."""

    def __init__(
        self: GloballyType,
        child: Node,
        unbound: bool = True,
        time_bound: Union[float, int] = 0.0,
        adapt_unbound: bool = True,
    ) -> None:
        super().__init__()
        self.child: Node = child
        self.unbound: bool = unbound
        self.time_bound: Union[float, int] = time_bound + 1
        self.adapt_unbound: bool = adapt_unbound

    def __str__(self: GloballyType) -> str:
        s0: str = "[0," + str(self.time_bound) + "]" if not self.unbound else ""
        s: str = "always" + s0 + " ( " + self.child.__str__() + " )"
        return s

    def time_depth(self: GloballyType) -> Union[float, int]:
        if self.unbound:
            return self.child.time_depth()
        else:
            return self.child.time_depth() + self.time_bound - 1

    def _boolean(self: GloballyType, x: Tensor) -> Tensor:
        z1: Tensor = self.child._boolean(x)
        if self.unbound:
            if self.adapt_unbound:
                z: Tensor
                _: Tensor
                z, _ = torch.cummin(torch.flip(z1, [2]), dim=2)
                z: Tensor = torch.flip(z, [2])
            else:
                z: Tensor
                _: Tensor
                z, _ = torch.min(z1, 2, keepdim=True)
        else:
            z: Tensor = torch.ge(1.0 - eventually((~z1).double(), self.time_bound), 0.5)
        return z

    def _quantitative(self: GloballyType, x: Tensor, normalize: bool = False) -> Tensor:
        z1: Tensor = self.child._quantitative(x, normalize)
        if self.unbound:
            if self.adapt_unbound:
                z: Tensor
                _: Tensor
                z, _ = torch.cummin(torch.flip(z1, [2]), dim=2)
                z: Tensor = torch.flip(z, [2])
            else:
                z: Tensor
                _: Tensor
                z, _ = torch.min(z1, 2, keepdim=True)
        else:
            z: Tensor = -eventually(-z1, self.time_bound)
        return z


class Eventually(Node):
    """Eventually node."""

    def __init__(
        self: EventuallyType,
        child: Node,
        unbound: bool = True,
        time_bound: Union[float, int] = 0.0,
        adapt_unbound: bool = True,
    ) -> None:
        super().__init__()
        self.child: Node = child
        self.unbound: bool = unbound
        self.time_bound: Union[float, int] = time_bound + 1
        self.adapt_unbound: bool = adapt_unbound

    def __str__(self: EventuallyType) -> str:
        s0: str = "[0," + str(self.time_bound) + "]" if not self.unbound else ""
        s: str = "eventually" + s0 + " ( " + self.child.__str__() + " )"
        return s

    def time_depth(self: EventuallyType) -> Union[float, int]:
        if self.unbound:
            return self.child.time_depth()
        else:
            return self.child.time_depth() + self.time_bound - 1

    def _boolean(self: EventuallyType, x: Tensor) -> Tensor:
        z1: Tensor = self.child._boolean(x)
        if self.unbound:
            if self.adapt_unbound:
                z: Tensor
                _: Tensor
                z, _ = torch.cummax(torch.flip(z1, [2]), dim=2)
                z: Tensor = torch.flip(z, [2])
            else:
                z: Tensor
                _: Tensor
                z, _ = torch.max(z1, 2, keepdim=True)
        else:
            z: Tensor = torch.ge(eventually(z1.double(), self.time_bound), 0.5)
        return z

    def _quantitative(
        self: EventuallyType, x: Tensor, normalize: bool = False
    ) -> Tensor:
        z1: Tensor = self.child._quantitative(x, normalize)
        if self.unbound:
            if self.adapt_unbound:
                z: Tensor
                _: Tensor
                z, _ = torch.cummax(torch.flip(z1, [2]), dim=2)
                z: Tensor = torch.flip(z, [2])
            else:
                z: Tensor
                _: Tensor
                z, _ = torch.max(z1, 2, keepdim=True)
        else:
            z: Tensor = eventually(z1, self.time_bound)
        return z
