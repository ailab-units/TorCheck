import numpy.random as rnd
from typing import Union

from torcheck import stl
from torcheck.stl import Node


class StlGenerator:
    def __init__(
        self,
        leaf_prob: float = 0.3,
        inner_node_prob: list = None,
        threshold_mean: float = 0.0,
        threshold_sd: float = 1.0,
        unbound_prob: float = 0.1,
        right_unbound_prob: float = 0.2,
        time_bound_max_range: float = 20,
        adaptive_unbound_temporal_ops: bool = True,
        max_timespan: int = 100,
    ):
        """
        leaf_prob
            probability of generating a leaf (always zero for root)
        node_types = ["not", "and", "or", "always", "eventually", "until"]
            Inner node types
        inner_node_prob
            probability vector for the different types of internal nodes
        threshold_mean
        threshold_sd
            mean and std for the normal distribution of the thresholds of atoms
        unbound_prob
            probability of a temporal operator to have a time bound o the type [0,infty]
        time_bound_max_range
            maximum value of time span of a temporal operator (i.e. max value of t in [0,t])
        adaptive_unbound_temporal_ops
            if true, unbounded temporal operators are computed from current point to the end of the signal, otherwise
            they are evaluated only at time zero.
        max_timespan
            maximum time depth of a formula.
        """

        # Address the mutability of default arguments
        if inner_node_prob is None:
            inner_node_prob = [0.166, 0.166, 0.166, 0.17, 0.166, 0.166]

        self.leaf_prob = leaf_prob
        self.inner_node_prob = inner_node_prob
        self.threshold_mean = threshold_mean
        self.threshold_sd = threshold_sd
        self.unbound_prob = unbound_prob
        self.right_unbound_prob = right_unbound_prob
        self.time_bound_max_range = time_bound_max_range
        self.adaptive_unbound_temporal_ops = adaptive_unbound_temporal_ops
        self.node_types = ["not", "and", "or", "always", "eventually", "until"]
        self.max_timespan = max_timespan

    def sample(self, nvars):
        """
        Samples a random formula with distribution defined in class instance parameters

        Parameters
        ----------
        nvars : number of variables of input signals
            how many variables the formula is expected to consider.

        Returns
        -------
        TYPE
            A random formula.

        """
        return self._sample_internal_node(nvars)

    def bag_sample(self, bag_size, nvars):
        """
        Samples a bag of bag_size formulae

        Parameters
        ----------
        bag_size : INT
            number of formulae.
        nvars : INT
            number of vars in formulae.

        Returns
        -------
        a list of formulae.

        """
        formulae = []
        for _ in range(bag_size):
            phi = self.sample(nvars)
            formulae.append(phi)
        return formulae

    def _sample_internal_node(self, nvars):
        # Declare & dummy-assign "idiom"
        node: Union[None, Node]
        node = None
        # choose node type
        nodetype = rnd.choice(self.node_types, p=self.inner_node_prob)
        while True:
            if nodetype == "not":
                n = self._sample_node(nvars)
                node = stl.Not(n)
            elif nodetype == "and":
                n1 = self._sample_node(nvars)
                n2 = self._sample_node(nvars)
                node = stl.And(n1, n2)
            elif nodetype == "or":
                n1 = self._sample_node(nvars)
                n2 = self._sample_node(nvars)
                node = stl.Or(n1, n2)
            elif nodetype == "always":
                n = self._sample_node(nvars)
                unbound, right_unbound, left_time_bound, right_time_bound = self._get_temporal_parameters()
                node = stl.Globally(
                    n, unbound, right_unbound, left_time_bound, right_time_bound, self.adaptive_unbound_temporal_ops
                )
            elif nodetype == "eventually":
                n = self._sample_node(nvars)
                unbound, right_unbound, left_time_bound, right_time_bound = self._get_temporal_parameters()
                node = stl.Eventually(
                    n, unbound, right_unbound, left_time_bound, right_time_bound, self.adaptive_unbound_temporal_ops
                )
            elif nodetype == "until":
                n1 = self._sample_node(nvars)
                n2 = self._sample_node(nvars)
                unbound, right_unbound, left_time_bound, right_time_bound = self._get_temporal_parameters()
                node = stl.Until(
                    n1, n2, unbound, right_unbound, left_time_bound, right_time_bound
                )

            if (node is not None) and (node.time_depth() < self.max_timespan):
                return node

    def _sample_node(self, nvars):
        if rnd.rand() < self.leaf_prob:
            # sample a leaf
            var, thr, lte = self._get_atom(nvars)
            return stl.Atom(var, thr, lte)
        else:
            return self._sample_internal_node(nvars)

    def _get_temporal_parameters(self):
        if rnd.rand() < self.unbound_prob:
            return True, False, 0, 0
        elif rnd.rand() < self.right_unbound_prob:
            return False, True, rnd.randint(self.time_bound_max_range), 1
        else:
            left_bound = rnd.randint(self.time_bound_max_range)
            return False, False, left_bound, rnd.randint(left_bound, self.time_bound_max_range) + 1

    def _get_atom(self, nvars):
        variable = rnd.randint(nvars)
        lte = rnd.rand() > 0.5
        threshold = rnd.normal(self.threshold_mean, self.threshold_sd)
        return variable, threshold, lte


class StlUniformGenerator:
        def __init__(
                self,
                leaf_prob=0.5,
                inner_node_prob=None,
                threshold_bounds=None,
                unbound_prob=0.1,
                time_bound_max_range=20,
                adaptive_unbound_temporal_ops=True,
                max_timespan=100,
        ):
            """
            leaf_prob
                probability of generating a leaf (always zero for root)
            node_types = ["not", "and", "or", "always", "eventually", "until"]
                Inner node types
            inner_node_prob
                probability vector for the different types of internal nodes
            threshold_mean
            threshold_sd
                mean and std for the normal distribution of the thresholds of atoms
            unbound_prob
                probability of a temporal operator to have a time bound of the type [0,infty]
            time_bound_max_range
                maximum value of time span of a temporal operator (i.e. max value of t in [0,t])
            adaptive_unbound_temporal_ops
                if true, unbounded temporal operators are computed from current point to the end of the signal, otherwise
                they are evaluated only at time zero.
            max_timespan
                maximum time depth of a formula.


            """

            # Address the mutability of default arguments
            if inner_node_prob is None:
                inner_node_prob = [0.2, 0.2, 0.2, 0.2, 0.2, 0.0]

            if threshold_bounds is None:
                threshold_bounds = [-3.0, 3.0]

            self.leaf_prob = leaf_prob
            self.inner_node_prob = inner_node_prob
            self.threshold_bounds = threshold_bounds
            self.unbound_prob = unbound_prob
            self.time_bound_max_range = time_bound_max_range
            self.adaptive_unbound_temporal_ops = adaptive_unbound_temporal_ops
            self.node_types = ["not", "and", "or", "always", "eventually", "until"]
            self.max_timespan = max_timespan

        def sample(self, nvars):
            """
            Samples a random formula with distribution defined in class instance parameters

            Parameters
            ----------
            nvars : number of variables of input signals
                how many variables the formula is expected to consider.

            Returns
            -------
            TYPE
                A random formula.

            """
            return self._sample_internal_node(nvars)

        def bag_sample(self, bag_size, nvars):
            """
            Samples a bag of bag_size formulae

            Parameters
            ----------
            bag_size : INT
                number of formulae.
            nvars : INT
                number of vars in formulae.

            Returns
            -------
            a list of formulae.

            """
            formulae = []
            for _ in range(bag_size):
                phi = self.sample(nvars)
                formulae.append(phi)
            return formulae

        def _sample_internal_node(self, nvars):
            # Declare & dummy-assing "idiom"
            node: Union[None, Node]
            node = None
            # choose node type
            nodetype = rnd.choice(self.node_types, p=self.inner_node_prob)
            while True:
                if nodetype == "not":
                    n = self._sample_node(nvars)
                    node = stl.Not(n)
                elif nodetype == "and":
                    n1 = self._sample_node(nvars)
                    n2 = self._sample_node(nvars)
                    node = stl.And(n1, n2)
                elif nodetype == "or":
                    n1 = self._sample_node(nvars)
                    n2 = self._sample_node(nvars)
                    node = stl.Or(n1, n2)
                elif nodetype == "always":
                    n = self._sample_node(nvars)
                    unbound, time_bound = self._get_temporal_parameters()
                    node = stl.Globally(
                        n, unbound, time_bound, self.adaptive_unbound_temporal_ops
                    )
                elif nodetype == "eventually":
                    n = self._sample_node(nvars)
                    unbound, time_bound = self._get_temporal_parameters()
                    node = stl.Eventually(
                        n, unbound, time_bound, self.adaptive_unbound_temporal_ops
                    )
                elif nodetype == "until":
                    raise NotImplementedError(
                        "Node for STL 'Until' operator not yet implemented!"
                    )

                if (node is not None) and (node.time_depth() < self.max_timespan):
                    return node

        def _sample_node(self, nvars):
            if rnd.rand() < self.leaf_prob:
                # sample a leaf
                var, thr, lte = self._get_atom(nvars)
                return stl.Atom(var, thr, lte)
            else:
                return self._sample_internal_node(nvars)

        def _get_temporal_parameters(self):
            if rnd.rand() < self.unbound_prob:
                return True, 0
            else:
                return False, rnd.randint(self.time_bound_max_range) + 1

        def _get_atom(self, nvars):
            variable = rnd.randint(nvars)
            lte = rnd.rand() > 0.5
            threshold = rnd.uniform(self.threshold_bounds[0], self.threshold_bounds[1])
            return variable, threshold, lte
