"""Module containing functions for reading input data and saving output data"""

import os.path
import sys
import numpy as np


def read_inp(path):
    """
    Reads an input file called "schrodinger.inp"

    Args:
        path (string): path to the input file

    Returns:
        data (dictionary): all parameter from the input file. Parameters are:
        mass, xMin, xMax, nPoint, first, last, interpol_method, interpol_num,
        x_decl and y_decl
    """

    data = {}

    try:
        fp = open(os.path.join(path, 'schrodinger.inp'), 'r')
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


def output_storage(first, last, potential, energy, w_func, exp_x, unc_x, x_points, directory):
    """
    Stores potential, eigenvalues, eigenfunctions,
    expectationvalues, uncertainties into output files.

    Args:
        first (float): first eigenvalue to include
        last (float): last eigenvalue to include
        potential (1d-array): interpolated potential V(x)
        energy (1d-array): energy eigenvalues
        w_func (array): normalized eigenfunctions
        exp_x (array): expectation value of position operator
        unc_x (1d-array): position uncertainty
        x_points (1d-array): coordinates for discretization points
        directory (string): location for saving output file
    """

    np.savetxt(os.path.join(directory, 'potential.dat'),
               np.transpose(np.array([x_points, potential(x_points)])))
    np.savetxt(os.path.join(directory, 'energies.dat'),
               np.transpose(energy[first-1:last]))
    x_points = np.reshape(x_points, (len(x_points), 1))
    np.savetxt(os.path.join(directory, 'wavefuncs.dat'),
               np.hstack((x_points, w_func)))
    np.savetxt(os.path.join(directory, 'expvalues.dat'),
               np.transpose(np.array([exp_x[first-1:last], unc_x[first-1:last]])))
