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
           lim_y=None, eigenmin=1, eigenmax=None, scalfac=1, extraspace=1):
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
        extraspace (int): addional space between eigenfunctions and ordinate axis.
    """
    if eigenmax is None:
        eigenmax = len(energies)

    plt.plot(x_val, potential, color="black")

    # adjusting x and y axis
    if lim_x is None:
        space = np.abs(np.amax(x_val) * 0.05 * extraspace)
        x_min = np.amin(x_val) - space
        x_max = np.amax(x_val) + space
        lim_x = (x_min, x_max)
        plt.xlim(lim_x)
    else:
        xmin, xmax = lim_x
        space = np.abs(xmax * 0.05 * extraspace)
        xmin = np.abs(xmin) - space
        xmax = np.abs(xmax) + space
        lim_x_extra_space = (xmin, xmax)
        plt.xlim(lim_x_extra_space)

    if lim_y is None:
        if np.abs(np.amin(potential)) < 0.05:
            y_min = -0.1
        else:
            y_min = np.amin(potential) * 1.1
        if np.abs(energies[-1]) < 0.2:
            y_max = energies[-1] * 2.5 + (np.amax(eigenfunctions[:, eigenmax])) * scalfac
        else:
            y_max = energies[-1] * 1.05 + (np.amax(eigenfunctions[:, eigenmax])) * scalfac
        lim_y = (y_min, y_max)
        plt.ylim(lim_y)
    else:
        plt.ylim(lim_y)

    for ii in range(eigenmin - 1, eigenmax):

        # plotting eigenfunctions in oscillating colours
        if ii % 2:
            color = "red"
        if not ii % 2:
            color = "blue"

        plt.plot(x_val, scalfac * eigenfunctions[:, ii] + energies[ii], color, linewidth=2)
        plt.hlines(energies[ii], x_min, x_max, color="grey")
        plt.plot(exp_values[ii], energies[ii], "x", color="green", )

    plt.title(r"Potential, eigenstates, $\langle x \rangle$", fontsize=14)
    plt.xlabel("x [Bohr]", fontsize=12)
    plt.ylabel("Energy [Hartree]", fontsize=12)

    return None


def plotuncertainty(potential, eigenfunctions, energies, uncertainties,
                    eigenmax, unclim_x=None, lim_y=None, scalfac=1):
    """Plotting uncertainty values of a 1d qm problem.

    Args:
        potential (array): potential to plot.
        eigenfunctions (array): eigenfunctions to plot.
        energies (array): eigenenergies to plot.
        uncertainties (array): uncertainty values to plot.
        eigenmax (int): last eigenstate to plot.
        unclim_x (tupel): first and last x-value to plot.
        lim_y (tupel): first and last y-value to plot.
        scalfac (float): scaling factor.
    """
    if eigenmax is None:
        eigenmax = len(energies)

    plt.plot(uncertainties, energies, "+", color="magenta", markersize=14, mew=2)

    if unclim_x is None:
        x_min = 0
        x_max = np.amax(uncertainties) * 1.05
        unclim_x = (x_min, x_max)
        plt.xlim(unclim_x)
    else:
        x_min, x_max = unclim_x
        plt.xlim(unclim_x)

    if lim_y is None:
        if np.abs(np.amin(potential)) < 0.2:
            y_min = -0.1
        else:
            y_min = np.amin(potential) * 1.1
        if np.abs(energies[-1]) < 0.2:
            y_max = energies[-1] * 2.5 + (np.amax(eigenfunctions[:, eigenmax])) * scalfac
        else:
            y_max = energies[-1] * 1.05 + (np.amax(eigenfunctions[:, eigenmax])) * scalfac
        lim_y = (y_min, y_max)
        plt.ylim(lim_y)
    else:
        plt.ylim(lim_y)

    plt.hlines(energies, x_min, x_max, color="grey")
    plt.yticks([])
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

    answer = None
    while answer not in ("y", "n"):
        answer = input("Do you prefer extra space between wavefunctions\n\
and left and right ordinate axis? [y/n]")
        if answer == "y":
            extraspace = 1
        elif answer == "n":
            extraspace = 0
        else:
            print("Please enter y or n.")

    print(">>> For the following plot settings, press ENTER without \
any inputs\nto use default settings <<<")

    lim_x = input("Please input the x-axis range as a tuple\n\
(DEFAULT: xMin, xMax of schrodinger.inp): ")

    lim_y = input("Please input the y-axis range as a tuple\n\
(DEFAULT: y-axis includes amin(potential) and amax(last eigenfunction): ")

    msg = "Please input the first and last eigenvalue to be \
plotted as a tuple\n(DEFAULT: first, last of schrodinger.inp): "
    eigenlim = input(msg)

    msg = "Please input a scaling factor for better visual representation\n\
(DEFAULT: 1, recommendation: 0.1 - 1.0): "
    try:
        scalefac = float(input(msg))
    except ValueError:
        scalefac = 1.0

    msg = "Please input the x-axis range for the uncertainty plot as a tuple\n\
(DEFAULT: x-axis will start at 0 and ends at max. uncertainty): "
    unclim_x = input(msg)

    # converting strings into tuples
    try:
        lim_x = tuple(float(x) for x in lim_x.split(","))
    except ValueError:
        lim_x = None

    try:
        lim_y = tuple(float(x) for x in lim_y.split(","))
    except ValueError:
        lim_y = None

    try:
        eigenlim = tuple(int(x) for x in eigenlim.split(","))
    except ValueError:
        eigenlim = None

    try:
        unclim_x = tuple(float(x) for x in unclim_x.split(","))
    except ValueError:
        unclim_x = None

    return direc, lim_x, lim_y, eigenlim, scalefac, unclim_x, extraspace


def display_subplots(x_val, potential, eigenfunctions, energies, expec_val,
                     lim_x, lim_y, eigenlim, scalefac, uncertainties,
                     unclim_x, extraspace):
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

    plt.figure(figsize=(7, 5))

    if eigenlim is None:
        first = 1
        last = len(energies)
        eigenlim = (first, last)

    plt.subplot(1, 2, 1)
    plotqm(x_val, potential, eigenfunctions, energies, expec_val,
           lim_x, lim_y, eigenlim[0], eigenlim[1], scalefac, extraspace)

    plt.subplot(1, 2, 2)
    plotuncertainty(potential, eigenfunctions, energies, uncertainties,
                    eigenlim[1], unclim_x, lim_y, scalefac)

    plt.show()
    return
