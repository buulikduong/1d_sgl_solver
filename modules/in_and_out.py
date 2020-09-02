""" Empty module for reading input data and saving output data """

import numpy as np

def read_inp(file):
    """Reading an input file schrodinger.inp

    Args:
        file: Path to the input file

    Retruns:
        dict: Dictionary containing all parameter from the input file
    """

    data = {}

    with open(file + 'schrodinger.inp', 'r') as fp:
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

    print(data)
    return data

read_inp('/home/dbuulik/1d_sgl_solver/application_examples/infinite_potential_well/')


