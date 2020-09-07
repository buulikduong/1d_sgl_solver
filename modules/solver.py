
"""
Module for solving 1 dimensional stationary Schrodinger equation \nand calculating expectation values of x.
"""

import numpy as np
import scipy.linalg

def solv(xMin, xMax, nPoint, mass, potential):
    """
    Routine for solving stationary Schroedinger equation in tridiagonal maxtrix form.

    Args:
        xMin: left value on x-axis
        xMax: right value on y-axis
        nPoint: number of discretization points on x-axis
        potential: array containing all potentials V(x)
        mass: particle mass

    Returns:
        eigen_val = Eigenvalue of the given problem
        w_function = nomalized wavefunction of the given problem
    """

    delta = (xMax - xMin) / (nPoint - 1)

    diagonal_main = 1/(mass*delta**2) + potential
    diagonal_sub = (1/(mass*delta**2)) + np.zeros(nPoint - 1)
    eigenvalue, eigenvector = scipy.linalg.eigh_tridiagonal(diagonal_main, diagonal_sub)

    #normalizing eigenvectors
    w_function = np.ones(eigenvector.shape)
    for ii in range(0, len(eigenvector[0])):
        norm_factor = 1/np.sqrt(sum(eigenvector[:, ii]**2))
        w_function[:, ii] = np.array([norm_factor*eigenvector[:, ii]])

    return eigenvalue, w_function


def exp_val(w_function, xMin, xMax, nPoint):
    """
    Routine for calculating expectation values and uncertainty of x.

        Args:
            w_function: normalized eigenvectors to given problem
            xMin: left value on x-axis
            xMax: right value on x-axis
            nPoint: number of discretization points on x-axis

        Returns:
            exp_x: array containing the expectation values
            unc_x: array containing the position uncertainty
    """

    delta = (xMax - xMin) / (nPoint - 1)
    x_i = np.linspace(xMin, xMax, nPoint)
    exp_x = np.ones(len(w_function[0]))
    exp_x_sqrt = np.ones(len(w_function[0]))

    for ii in range(0, np.len(w_function[0])):
        exp_x[ii] = delta * np.sum(w_function[:, ii] * x_i * w_function[:, ii])
        exp_x_sqrt[ii] = delta * np.sum(w_function[:, ii] * x_i**2 * w_function[:, ii])

    unc_x = np.sqrt(exp_x_sqrt - exp_x**2)

    return exp_x, unc_x
