"""Module for reading input data and saving output data."""

import sys
import numpy as np


def read_inp(path):
    """
    Reading an input file schrodinger.inp.

    Args:
        path: path to the input file

    Returns:
        data: dictionary containing all parameter from the input file
    """

    data = {}

    try:
        fp = open(path + 'schrodinger.inp', 'r')
    except OSError:
        print("Input file can not be read.")
        print("Please check location and permission rights.")
        sys.exit(1)
    try:
        line = fp.readline()
        data['mass'] = float(line.split()[0])
        line = fp.readline()
        data['xMin'] = float(line.split()[0])
        data['xMax'] = float(line.split()[1])
        data['nPoint'] = int(line.split()[2])
        line = fp.readline()
        data['first'] = int(line.split()[0])
        data['last'] = int(line.split()[1])
        line = fp.readline()
        data['interpol_method'] = line.split()[0]
        line = fp.readline()
        data['interpol_num'] = int(line.split()[0])
        lines = np.loadtxt(fp.readlines()[0:])
        data['x_decl'] = lines[:, 0]
        data['y_decl'] = lines[:, 1]
    except IndexError:
        print("schrodinger.inp do not have the correct format.")
        print("Please check your input file.")
    return data


def output_storage(potential, energy, w_function, exp_val, sigma_x, x_points, directory):
    """
    Storing potential, eigenvalues, eigenfunctions,
    expectationvalues,cuncertainty into output files.

    Args:
        potential (1d-array): interpolated potential V(x)
        energy (1d-array): energy eigenvalues
        w_function (array): normalized eigenfunctions
        exp_val (array): expectation value of position operator
        sigma_x (1d-array): position uncertainty
        x_points (1d-array): coordinates for discretization points
        directory: location for saving output file
    """

    np.savetxt(str(directory) + 'potential.dat',
               np.transpose(np.array([x_points, potential(x_points)])))
    np.savetxt(str(directory) + 'energies.dat',
               np.transpose(energy))
    x_points = np.reshape(x_points, (len(x_points), 1))
    np.savetxt(str(directory) + 'wavefuncs.dat',
               np.hstack((x_points, w_function)))
    np.savetxt(str(directory) + 'expvalues.dat',
               np.transpose(np.array([exp_val, sigma_x])))
