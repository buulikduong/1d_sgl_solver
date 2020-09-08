"""
Module for solving 1 dimensional stationary Schrodinger equation,
calculating expectation values of operator x and corresponding uncertainty.
"""

import numpy as np
import scipy.linalg


def solv(xmin, xmax, npoint, mass, potential):
    """
    Routine for solving stationary Schroedinger equation
    in tridiagonal maxtrix form.

    Args:
        xmin (float): left value on x-axis
        xmax (float): right value on x-axis
        npoint (int): number of discretization points for x-axis
        potential (array): interpolated potentials
        mass (float): particle mass

    Returns:
        eigen_val ((M,)array): eigenvalue of the given problem
        w_function ((M, M)array): corresponding nomalized wavefunction
    """

    delta = (xmax - xmin)/(npoint - 1)

    diagonal_main = 1/(mass*delta**2) + potential
    diagonal_sub = 1/(mass*delta**2) + np.zeros(npoint - 1)
    eigenvalue, eigenvector = scipy.linalg.eigh_tridiagonal(diagonal_main,
                                                            diagonal_sub)

    # normalizing eigenvectors
    w_function = np.ones(eigenvector.shape)
    for ii in range(0, len(eigenvector[0])):
        norm_factor = 1/np.sqrt(sum(eigenvector[:, ii]**2))
        w_function[:, ii] = np.array([norm_factor*eigenvector[:, ii]])

    return eigenvalue, w_function


def exp_val(w_function, xmin, xmax, npoint):
    """
    Routine for calculating expectation values and uncertainty of x.

        Args:
            w_function (array): normalized eigenvectors
            xmin (float): left value on x-axis
            xmax (float): right value on x-axis
            npoint (int): number of discretization points for x-axis

        Returns:
            exp_x (array): expectation values
            unc_x (array): position uncertainty
    """

    delta = (xmax - xmin)/(npoint - 1)
    x_i = np.linspace(xmin, xmax, npoint)
    exp_x = np.ones(len(w_function[0]))
    exp_x_sqrt = np.ones(len(w_function[0]))

    for ii in range(0, np.len(w_function[0])):
        exp_x[ii] = delta * np.sum(w_function[:, ii] * x_i * w_function[:, ii])
        exp_x_sqrt[ii] = delta * np.sum(w_function[:, ii]**2 * x_i**2)

    unc_x = np.sqrt(exp_x_sqrt - exp_x**2)

    return exp_x, unc_x
