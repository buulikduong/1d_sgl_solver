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
        eigenfunctions (array): calculated eigenfunctions
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


def plotqm(x_val, potential, eigenfunctions, energies, exp_values, lim_x=None,
           lim_y=None, eigenmin=0, eigenmax=len(energies), scalfac=1):
    """Function that plots the solution of the 1d QM problem

    Args:
        x_val (array): x-values of the problem
        eigenfunctions (array): calculated eigenfunctions
        energies (array): Eigenenegies of the eigenfunctions
        potential (array): the potential of the problem
        expec_val (array): Erwartungswerte
        xMin (float): minimum x-value to plot
        xMax (float): max x-value to plot
        eigenmin (int): first eigenstate to be plotted
        eigenmax (int): last eigenstate to be plotted
        scalfac (float): scling factor for better readability of the plot
        fsize (int): fontsize
    """
    plt.plot(x_val, potential, color="black")

    if lim_x is None:
        x_min, x_max = plt.xlim()
    else:
        x_min, x_max = lim_x
        plt.xlim(lim_x)

    if lim_y is not None:
        plt.ylim(lim_y)

    for ii in range(eigenmin - 1, eigenmax):
        if ii % 2:
            color = "blue"
        if not ii % 2:
            color = "red"

        plt.plot(x_val, scalfac * eigenfunctions[:, ii] + energies[ii], color)
        plt.hlines(energies[ii], x_min, x_max, color="grey")
        plt.plot(exp_values[ii], energies[ii], "x", color="green", )

    plt.title(r"Potential, eigenstates, $\langle x \rangle$", fontsize=14)
    plt.xlabel("x [Bohr]", fontsize=12)
    plt.ylabel("Energy [Hartree]", fontsize=12)

    return None
