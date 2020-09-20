"""Module containing functions for plotting the solutions of the qm problem"""

import os.path
import matplotlib.pyplot as plt
import numpy as np


def readplotdata(direc):
    """Reads the data from the output files and returns the data
    in arrays.

    Args:
        direc (string): directory where data is located.

    Returns:
        x_val (array): x-values of the 1d-problem.
        potential (array): the potential of the problem.
        eigenfunctions (array): eigenfunctions of the problem.
        energies (array): eigenenegies of the eigenfunctions.
        expec_val (array): the expected values of the eigenfunctions.
        uncertainties (array): uncertainty values for every eigenfunction.
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


def plotqm(x_val, potential, eigenfunctions, energies, exp_values, lim_x=None,
           lim_y=None, eigenmin=1, eigenmax=None, scalfac=1):
    """Plots the eigenfunctions, eigenenergies and expected
    values of a 1d qm problem.

    Args:
        x_val (array): x-values of the problem.
        eigenfunctions (array): eigenfunctions to plot.
        energies (array): eigenenegies to plot.
        potential (array): potential to plot.
        expec_val (array): expected values to plot.
        xMin (float): min x-value to plot.
        xMax (float): max x-value to plot.
        eigenmin (int): first eigenstate to plot.
        eigenmax (int): last eigenstate to plot.
        scalfac (float): scaling factor for better readability of the plot.
    """
    if eigenmax is None:
        eigenmax = len(energies)

    plt.plot(x_val, potential, color="black")

    # adjusting x and y axis
    if lim_x is None:
        x_min, x_max = plt.xlim()
    else:
        x_min, x_max = lim_x
        plt.xlim(lim_x)

    if lim_y is not None:
        plt.ylim(lim_y)

    for ii in range(eigenmin - 1, eigenmax):

        # plotting eigenfunctions in oscillating colours
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


def plotuncertainty(energies, uncertainties, unclim_x=None, lim_y=None):
    """Plotting uncertainty values of a 1d qm problem.

    Args:
        energies (array): eigenenergies to plot.
        uncertainties (array): uncertainty values to plot.
        unclim_x (tupel): first and last x-value to plot.
        lim_y (tupel): first and last y-value to plot.
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


def _check_dir():
    """Checks if the plottable data is located in the same folder
    as the main function, by checking if wavefuncs.dat is present.

    Returns:
        isdir (bool): is plottable data in default directory
    """

    try:
        fp = open("wavefuncs.dat", "r")
    except FileNotFoundError:
        msg = "Plottable data not found or incomplete in default directory."
        print(msg)
        isdir = False
        return isdir
    else:
        fp.close()
        isdir = True
        return isdir


def user_inp():
    """Reads user inputs for plot options.

    Returns:
        direc (string): path to plot data.
        lim_x (tuple): x-axis-range.
        lim_y (tuple): y-axis-range.
        eigenmin (int): first eigenvalue to be plotted.
        eigenmax (int): last eigenvalue to be plotted.
    """

    # check if plottable data is located in default directory
    isdir = _check_dir()

    if isdir is False:
        msg = ("Please input the directory where the plottable\
data is located: ")
        direc = input(msg)

    lim_x = input("Please input the x-axis range as a tuple: ")
    lim_y = input("Please input the y-axis range as a tuple: ")

    msg = "Please input the first and last eigenvalue \
to be plotted as a tuple: "
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


def display_subplots(x_val, potential, eigenfunctions, energies, expec_val,
                     lim_x, lim_y, eigenlim, scalefac, uncertainties,
                     unclim_x):
    """Displays plots of eigenfunctions, eigenenergies, expected values and
    uncertainty values in two subplots.

    Args:
        x_val (array): x-values of the problem.
        eigenfunctions (array): eigenfunctions to plot.
        energies (array): eigenenegies to plot.
        potential (array): potential to plot.
        expec_val (array): expected values to plot.
        xMin (float): min x-value to plot.
        xMax (float): max x-value to plot.
        eigenlimn (tuple): first and last eigenstate to plot.
        scalfac (float): scaling factor for better readability of the plot.
        uncertainties (array): uncertainty values to plot.
        unclim_x (tupel): first and last x-value to plot.
        """

    plt.figure(figsize=(7, 4.5))

    plt.subplot(1, 2, 1)
    plotqm(x_val, potential, eigenfunctions, energies, expec_val,
           lim_x, lim_y, eigenlim[0], eigenlim[1], scalefac)

    plt.subplot(1, 2, 2)
    plotuncertainty(energies, uncertainties, unclim_x, lim_y)

    plt.show()
    return
