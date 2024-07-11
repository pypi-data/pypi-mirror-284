import ot as pot



def solve_ot(x, y, 𝜀, a=None, b=None):
    # you can also try "sinkhorn_stabilized", this is a bit faster but less stable for small 𝜀
    if a == None:
        a = pot.unif(x.shape[0])
    if b == None:
        b = pot.unif(y.shape[0])
    method = "sinkhorn_log"
    P = pot.sinkhorn(
        a,
        b,
        pot.dist(x, y),
        𝜀,
        method=method,
        
        numItermax=1000,
    )
    
    return P
'''
from ott.geometry import pointcloud
from ott.problems.linear import linear_problem
from ott.solvers.linear import sinkhorn
import jax
import torch
import math
from functools import partial
from typing import Optional

import numpy as np


@jax.jit
def solve_ott(x, y, a=None, b=None, 𝜀=None, max_iterations=1000):
    n = x.shape[0]
    if a == None:
        a = pot.unif(x.shape[0])
    if b == None:
        b = pot.unif(y.shape[0])
    if 𝜀 == None:
        geom = pointcloud.PointCloud(x, y, epsilon=pointcloud.PointCloud(x, y).mean_cost_matrix * 0.05)    
    else:
        geom = pointcloud.PointCloud(x, y, epsilon=𝜀)
    prob = linear_problem.LinearProblem(geom, a=a, b=b)
    solver = sinkhorn.Sinkhorn(
        #threshold=threshold,
        norm_error=2,
        lse_mode=True,
        max_iterations=max_iterations,
    )
    out = solver(prob)
    return np.asarray(out.matrix)

class OTPlanSampler:
    """OTPlanSampler implements sampling coordinates according to an OT plan (wrt squared Euclidean
    cost) with different implementations of the plan calculation."""

    def __init__(
        self,
        method: str,
        reg: float = 0.05,
        reg_m: float = 1.0,
        normalize_cost=False,
        max_iterations=10,
        **kwargs,
    ):
        # ot_fn should take (a, b, M) as arguments where a, b are marginals and
        # M is a cost matrix
        self.method = method
        if method == "exact":
            self.ot_fn = pot.emd
        elif method == "sinkhorn":
            #self.ot_fn = partial(pot.sinkhorn, reg=reg, method="sinkhorn_log", numItermax=1000, )
            self.ot_fn = partial(solve_ott, 𝜀=reg,  max_iterations=max_iterations)
        elif method == "unbalanced":
            self.ot_fn = partial(pot.unbalanced.sinkhorn_knopp_unbalanced, reg=reg, reg_m=reg_m)
        elif method == "partial":
            self.ot_fn = partial(pot.partial.entropic_partial_wasserstein, reg=reg)
        else:
            raise ValueError(f"Unknown method: {method}")
        self.reg = reg
        self.reg_m = reg_m
        self.normalize_cost = normalize_cost
        self.kwargs = kwargs

    def get_map(self, x0, x1):
        """Compute the OT plan (wrt squared Euclidean cost) between a source and a target
        minibatch.

        Parameters
        ----------
        x0 : Tensor, shape (bs, *dim)
            represents the source minibatch
        x1 : Tensor, shape (bs, *dim)
            represents the source minibatch

        Returns
        -------
        p : numpy array, shape (bs, bs)
            represents the OT plan between minibatches
        """
        
        if self.method == 'exact':
            a, b = pot.unif(x0.shape[0]), pot.unif(x1.shape[0])
            if x0.dim() > 2:
                x0 = x0.reshape(x0.shape[0], -1)
            if x1.dim() > 2:
                x1 = x1.reshape(x1.shape[0], -1)
            x1 = x1.reshape(x1.shape[0], -1)
            M = torch.cdist(x0, x1) ** 2
            if self.normalize_cost:
                M = M / M.max()  # should not be normalized when using minibatches
            p = self.ot_fn(a, b, M.detach().cpu().numpy())
        elif self.method == 'sinkhorn':
            p = self.ot_fn(x0, x1)
        if not np.all(np.isfinite(p)):
            print("ERROR: p is not finite")
            print(p)
            print("Cost mean, max", M.mean(), M.max())
            print(x0, x1)
        return p

    def sample_map(self, pi, batch_size):
        r"""Draw source and target samples from pi  $(x,z) \sim \pi$

        Parameters
        ----------
        pi : numpy array, shape (bs, bs)
            represents the source minibatch
        batch_size : int
            represents the OT plan between minibatches

        Returns
        -------
        (i_s, i_j) : tuple of numpy arrays, shape (bs, bs)
            represents the indices of source and target data samples from $\pi$
        """
        p = pi.flatten()
        p = p / p.sum()
        choices = np.random.choice(pi.shape[0] * pi.shape[1], p=p, size=batch_size)
        return np.divmod(choices, pi.shape[1])

    def sample_plan(self, x0, x1):
        r"""Compute the OT plan $\pi$ (wrt squared Euclidean cost) between a source and a target
        minibatch and draw source and target samples from pi $(x,z) \sim \pi$

        Parameters
        ----------
        x0 : Tensor, shape (bs, *dim)
            represents the source minibatch
        x1 : Tensor, shape (bs, *dim)
            represents the source minibatch

        Returns
        -------
        x0[i] : Tensor, shape (bs, *dim)
            represents the source minibatch drawn from $\pi$
        x1[j] : Tensor, shape (bs, *dim)
            represents the source minibatch drawn from $\pi$
        """
        pi = self.get_map(x0, x1)
        i, j = self.sample_map(pi, x0.shape[0])
        return x0[i], x1[j]

    def sample_plan_with_labels(self, x0, x1, y0=None, y1=None):
        r"""Compute the OT plan $\pi$ (wrt squared Euclidean cost) between a source and a target
        minibatch and draw source and target labeled samples from pi $(x,z) \sim \pi$

        Parameters
        ----------
        x0 : Tensor, shape (bs, *dim)
            represents the source minibatch
        x1 : Tensor, shape (bs, *dim)
            represents the target minibatch
        y0 : Tensor, shape (bs)
            represents the source label minibatch
        y1 : Tensor, shape (bs)
            represents the target label minibatch

        Returns
        -------
        x0[i] : Tensor, shape (bs, *dim)
            represents the source minibatch drawn from $\pi$
        x1[j] : Tensor, shape (bs, *dim)
            represents the target minibatch drawn from $\pi$
        y0[i] : Tensor, shape (bs, *dim)
            represents the source label minibatch drawn from $\pi$
        y1[j] : Tensor, shape (bs, *dim)
            represents the target label minibatch drawn from $\pi$
        """
        pi = self.get_map(x0, x1)
        i, j = self.sample_map(pi, x0.shape[0])
        return (
            x0[i],
            x1[j],
            y0[i] if y0 is not None else None,
            y1[j] if y1 is not None else None,
        )

    def sample_trajectory(self, X):
        """Compute the OT trajectories between different sample populations moving from the source
        to the target distribution.

        Parameters
        ----------
        X : Tensor, (bs, times, *dim)
            different populations of samples moving from the source to the target distribution.

        Returns
        -------
        to_return : Tensor, (bs, times, *dim)
            represents the OT sampled trajectories over time.
        """
        times = X.shape[1]
        pis = []
        for t in range(times - 1):
            pis.append(self.get_map(X[:, t], X[:, t + 1]))

        indices = [np.arange(X.shape[0])]
        for pi in pis:
            j = []
            for i in indices[-1]:
                j.append(np.random.choice(pi.shape[1], p=pi[i] / pi[i].sum()))
            indices.append(np.array(j))

        to_return = []
        for t in range(times):
            to_return.append(X[:, t][indices[t]])
        to_return = np.stack(to_return, axis=1)
        return to_return
'''