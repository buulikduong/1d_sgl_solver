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

    path_en = os.path.join(direc, "energies.dat")
    path_pot = os.path.join(direc, "potential.dat")
    path_wfuncs = os.path.join(direc, "wavefuncs.dat")
    path_expec_val = os.path.join(direc, "expvalues.dat")

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


def _plotqm(x_val, potential, eigenfunctions, energies, exp_values, lim_x=None,
            lim_y=None, eigenmin=0, eigenmax=None, scalfac=1):
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
    if eigenmax is None:
        eigenmax = len(energies)

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
            color = "red"
        if not ii % 2:
            color = "blue"

        plt.plot(x_val, scalfac * eigenfunctions[:, ii] + energies[ii], color)
        plt.hlines(energies[ii], x_min, x_max, color="grey")
        plt.plot(exp_values[ii], energies[ii], "x", color="green", )

    plt.title(r"Potential, eigenstates, $\langle x \rangle$", fontsize=14)
    plt.xlabel("x [Bohr]", fontsize=12)
    plt.ylabel("Energy [Hartree]", fontsize=12)

    return None


def _plotuncertainty(energies, uncertainties, unclim_x=None, lim_y=None):
    """function for plotting uncertainty values of a QM problem
    Args:
        energies (array): calculated energies of qm problem
        uncertainties (array): calculated uncertainty for each eigenstate
        unclim_x (tupel): first and last x-value to plot
        lim_y (tupel): first and last y-value to plot
    """

    plt.plot(uncertainties, energies, "+", color="pink", markersize=16, mew=2)

    if unclim_x is None:
        x_min, x_max = plt.xlim()
    else:
        x_min, x_max = unclim_x
        plt.xlim(unclim_x)

    if lim_y is not None:
        plt.ylim(lim_y)

    plt.hlines(energies, x_min, x_max, color="grey")

    plt.title(r"$\sigma_x$", fontsize=14)
    plt.xlabel("[Bohr]", fontsize=12)

    return None


def check_dir():
    """function that checks if the plottable data is located in the same folder
    as the main function

    Returns:
        isdir (bool): is plottable data in default directory
    """

    try:
        fp = open("potential.dat", "r")
    except FileNotFoundError:
        msg = "Plottable data not found or incomplete in default directory."
        print(msg)
        isdir = False
        return isdir
    else:
        fp.close()
        isdir = True
        return isdir


def user_inp(isdir):
    """function that reads user-inputs, which decide how the plots are gonna
       look like
       Args:
           isdir (bool): is plottable data in default directory
        Returns:
            direc (string): path where the data to be plotted is located
            lim_x (tuple): x-axis-range
            lim_y (tuple): y-axis-range
            eigenmin (int): first eigenvalue to be plotted
            eigenmax (int): last eigenvalue to be plotted
    """

    if isdir is False:
        msg = ("Please input the directory where the plottable\
data is located: ")
        direc = input(msg)

    lim_x = input("Please input the x-axis range as a tuple: ")
    lim_y = input("Please input the y-axis range as a tuple: ")

    msg ="Please input the first and last eigenvalue\
to  be plotted as a tuple: "
    eigenlim = input(msg)

    msg = "Please input a scaling factor for better visual representation: "
    scalefac = float(input(msg))

    msg = "Please input the x-axis range for the uncertainty plot as a tuple: "
    unclim_x = input(msg)

    # converting strings into tuples
    lim_x = tuple(float(x) for x in lim_x.split(","))
    lim_y = tuple(float(x) for x in lim_y.split(","))
    eigenlim = tuple(int(x) for x in eigenlim.split(","))
    unclim_x = tuple(float(x) for x in unclim_x.split(","))

    return direc, lim_x, lim_y, eigenlim, scalefac, unclim_x


def display_plots(x_val, potential, eigenfunctions, energies, expec_val, lim_x,
                  lim_y, eigenlim, scalefac, uncertainties, unclim_x):
    plt.figure(figsize=(7, 4.5))

    plt.subplot(1, 2, 1)
    _plotqm(x_val, potential, eigenfunctions, energies, expec_val,
            lim_x, lim_y, eigenlim[0], eigenlim[1], scalefac)

    plt.subplot(1, 2, 2)
    _plotuncertainty(energies, uncertainties, unclim_x, lim_y)
    plt.show()
    return
