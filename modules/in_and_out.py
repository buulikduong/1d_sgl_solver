""" Module/routine for reading input data and saving output data """

import sys
import numpy as np

def read_inp(path):
    """Reading an input file schrodinger.inp

    Args:
        path: Path to the input file

    Returns:
        data: Dictionary containing all parameter from the input file
    """

    data = {}

    try:
        fp = open(path + 'schrodinger.inp', 'r')
    except OSError:
        print("Input file can not be read.\nPlease check location and permission rights.")
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
        print("schrodinger.inp do not have the correct format.\nPlease check your input file.")
    print(data)
    return data

def output_storage(potential, energy, w_function, exp_val, sigma_x, xaxis, directory):
    """Saving potential, eigenvalues, eigenfunctions, expectationvalues, uncertainty into output files

    Args:
        potential: potential V(x) of the given problem
        energy: eigenvalues of energies
        w_function: standardised eigenfunction
        exp_val: expectation value of x
        sigma_x: uncertainty of x
        x_axis: values of x
        directory: location for saving output file
    """

    np.savetxt(directory + 'potentialdat', np.transpose(np.array([xaxis, potential(xaxis)]))
    np.savetxt(directory + 'energies.dat', np.transpose(np.array([energy])))
    xaxis = np.reshape(xaxis, (len(xaxis), 1))
    np.savetxt(directory + 'wavefuncs.dat', np.hstack((xaxis, w_functions))
    np.savetxt(directory + 'expvalues.dat', np.transpose(np.array([exp_val, sigma_x])))