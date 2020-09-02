""" Empty module for reading input data and saving output data """

import sys
import numpy as np

def read_inp(file):
    """Reading an input file schrodinger.inp

    Args:
        file: Path to the input file

    Retruns:
        dict: Dictionary containing all parameter from the input file
    """

    data = {}

    try:
        fp = open(file + 'schrodinger.inp', 'r')
    except OSError:
        print("Input file can not be read.\nPlease check location and permission rights.")
        sys.exit(1)
    try:
        line = fp.readline()
        data['mass'] = line.split()[0]
        line = fp.readline()
        data['xMin'] = line.split()[0]
        data['xMax'] = line.split()[1]
        data['nPoint'] = line.split()[2]
        line = fp.readline()
        data['first'] = line.split()[0]
        data['last'] = line.split()[1]
        line = fp.readline()
        data['interpol_method'] = line.split()[0]
        line = fp.readline()
        data['interpol_num'] = line.split()[0]
        lines = np.loadtxt(fp.readlines()[0:])
        data['x_decl'] = lines[:, 0]
        data['y_decl'] = lines[:, 1]
    except IndexError:
        print("schrodinger.inp do not have the correct format.\nPlease check your input file.")
    print(data)
    return data

read_inp('/home/dbuulik/1d_sgl_solver/application_examples/infinite_potential_well/')
