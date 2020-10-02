"""
Module containing functions for solving the 1 dimensional stationary
Schrodinger equation and calculating expectation values of operator x
and corresponding uncertainties.
"""

import numpy as np
from scipy import linalg
from scipy import sparse


def solv(xmin, xmax, npoint, mass, potential, first, last):
    """
    Routine for solving stationary Schroedinger equation
    in tridiagonal maxtrix form for a given potential.

    Args:
        xmin (float): left value on x-axis.
        xmax (float): right value on x-axis.
        npoint (int): number of discretization points for x-axis.
        potential (function): interpolated function.
        mass (float): particle mass.

    Returns:
        eigen_val ((M,)array): eigenvalue of the given problem
        eigen_vec ((M, M)array): corresponding eigenvectors
        x_points (1d-array): coordinates for discretization points
    """
    # creating true symmetric tridiagonal matrix
    x_points = np.linspace(xmin, xmax, npoint)
    delta = np.abs(x_points[1] - x_points[0])
    diagonal_main = np.array([1/(mass*delta**2) + potential(ii) for ii in x_points])
    diagonal_sub = -1/(2*mass*delta**2)*np.ones(npoint, dtype=float)
    diags = np.array([diagonal_main, diagonal_sub, diagonal_sub])
    positions = np.array([0, -1, 1])
    tridiagonal = sparse.spdiags(diags, positions, npoint, npoint).toarray()

    # solving tridiagonal matrix
    eigen_val, eigen_vec = linalg.eigh(tridiagonal, eigvals=(first - 1, last - 1))
    return eigen_val, eigen_vec, x_points


def norm(eigenvectors, xmin, xmax, npoint):
    """
    Routine for normalizing the eigenvectors of the given qm problem.

    Args:
        eigenvectors (array): eigenvectors of the given qm problem.
        xmin (float): left value on x-axis.
        xmax (float): right value on x-axis.
        npoint (int): number of discretization points for x-axis.

    Returns:
        w_func (array): corresponding normalized wavefunctions
    """
    x_points = np.linspace(xmin, xmax, npoint)
    delta = np.abs(x_points[1] - x_points[0])
    w_func = np.ones(eigenvectors.shape, dtype=float)
    for ii in range(0, len(eigenvectors[0])):
        norm_factor = 1/np.sqrt(sum(np.abs(eigenvectors[:, ii])**2)*delta)
        w_func[:, ii] = np.array([norm_factor*eigenvectors[:, ii]])

    return w_func


def exp_val(w_func, xmin, xmax, npoint):
    r"""
    Routine for calculating expectation values $\Delta x$ and
    position uncertainty $\sigma$.

        Args:
            w_func (array): normalized eigenvectors.
            xmin (float): left value on x-axis.
            xmax (float): right value on x-axis.
            npoint (int): number of discretization points for x-axis.

        Returns:
            exp_x (1d-array): expectation values
            unc_x (1d-array): position uncertainty
    """
    x_points = np.linspace(xmin, xmax, npoint)
    delta = np.abs(x_points[1] - x_points[0])
    exp_x = np.ones(len(w_func[0]))
    exp_x_sqrt = np.ones(len(w_func[0]))

    for ii in range(0, len(w_func[0])):
        exp_x[ii] = delta * np.sum(w_func[:, ii] * x_points * w_func[:, ii])
        exp_x_sqrt[ii] = delta * np.sum(w_func[:, ii]**2 * x_points**2)

    unc_x = np.sqrt(exp_x_sqrt - exp_x**2)

    return exp_x, unc_x
