"""Module containing functions connected to plotting the solutions"""

import os.path
import matplotlib.pyplot as plt
import numpy as np


def readplotdata(direc):
    """Function that selects the directory of the data to be plotted

    Args:
        direc (string): directory where data is located

    Returns:
        x_val (array): x-values of the 1d-problem
        potential (array): the potential of the problem
        eigenfunctions (array): the calculated eigenfunctions
        energies (array): energy values of the eigenfunctions
        expec_val (array): the expected values of the eigenfunctions
        uncertainties (array): uncertainty values for every eigenfunction
    """

    dirname = "application_examples/" + direc

    path_en = os.path.join(dirname, "energies.dat")
    path_pot = os.path.join(dirname, "potential.dat")
    path_wfuncs = os.path.join(dirname, "wavefuncs.dat")
    path_expec_val = os.path.join(dirname, "expvalues.dat")

    energies = np.loadtxt(path_en)
    potential = np.loadtxt(path_pot)
    wavefuncs = np.loadtxt(path_wfuncs)
    expvalues = np.loadtxt(path_expec_val)

    x_val = potential[:, 0]
    potential = potential[:, 1]
    eigenfunctions = wavefuncs[:, 1:]
    exp_values = expvalues[:, 0]
    uncertainties = expvalues[:, 1]

    return x_val, potential, eigenfunctions, energies, exp_values, uncertainties
