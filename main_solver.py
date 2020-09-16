#!/usr/bin/env python
"""Executable script for solving stationary schrodinger equation"""

import argparse
from modules import in_and_out, interpolator, solver

_DESCRIPTION = "Solving schrodinger equation for a given potential."


def main():
    """
    Main routine for solving schrodinger equation
    """
    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    msg = 'Path to input file.'
    parser.add_argument('-i', '--input', type=str,
                        default='./application_examples/infinite_potential_well/', help=msg)
    msg = 'Path to output file'
    parser.add_argument('-o', '--output', type=str,
                        default='./application_examples/infinite_potential_well/', help=msg)
    args = parser.parse_args()

    parameter = in_and_out.read_inp(args.input)

    int_pot = interpolator.interpolator(parameter['x_decl'],
                                        parameter['y_decl'],
                                        parameter['interpol_method'])

    eigenvalue, w_function, x_points = solver.solv(parameter['xMin'],
                                                   parameter['xMax'],
                                                   parameter['nPoint'],
                                                   parameter['mass'], int_pot)

    exp_x, unc_x = solver.exp_val(w_function, parameter['xMin'],
                                  parameter['xMax'],
                                  parameter['nPoint'])

    in_and_out.output_storage(parameter['first'], parameter['last'],
                              int_pot, eigenvalue, w_function, exp_x, unc_x,
                              x_points, args.output)


if __name__ == '__main__':
    main()
