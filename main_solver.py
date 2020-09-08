#!/usr/bin/env python

import argparse
from modules import in_and_out

_DESCRIPTION = "Solving schrodinger equation for a given potential."


def main():
    parser = argparse.ArgumentParser(description=_DESCRIPTION)
    msg = 'Path to input file.'
    parser.add_argument('-i', '--input', type=str,
                        default='/home/dbuulik/1d_sgl_solver/application_examples/infinite_potential_well/', help=msg)
    args = parser.parse_args()
    parameter = in_and_out.read_inp(args.input)
    print(parameter['nPoint'])


if __name__ == '__main__':
    main()
