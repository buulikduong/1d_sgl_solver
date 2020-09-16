"""
Module for calculating analytic solution of potential and eigenvalues
for the infinite and finite potential well and for the harmonic osciallator.
"""

import os.path
import numpy as np


def _potential_inifinite_potwell():
    """Calcultes the potential for the infinite potential well"""
    potential = np.zeros(1999)
    directory = './../application_examples/infinite_potential_well/'
    file = 'potential.ref'
    np.savetxt(os.path.join(directory, file), potential)

    return potential


def _potential_fininite_potwell():
    """Calculates the potential for the finite potential well."""
    pot_1 = np.zeros((750,), dtype=float)
    pot_2 = -10 * np.ones((499,), dtype=float)
    pot_3 = np.zeros((750, ), dtype=float)
    potential = np.concatenate((pot_1, pot_2, pot_3), axis=0)
    directory = './../application_examples/finite_potential_well/'
    file = 'potential.ref'
    np.savetxt(os.path.join(directory, file), potential)

    return potential


def _potential_harmonic_potwell():
    """Calculates the potential for a harmonic oscillator."""
    x_points = np.linspace(-5, 5, 1999)
    potential = 0.5 * x_points**2
    directory = './../application_examples/harmonic_potential_well/'
    file = 'potential.ref'
    np.savetxt(os.path.join(directory, file), potential)

    return potential


def _eigenvalue_infinite_potwell():
    """Calculates the energy eigenvalues of the infinite potential well."""
    eig_val = np.ones((5, ), dtype=float)
    for ii in range(0, 5):
        eig_val[ii] = ii**2 * np.pi**2 / (2 * 2 * 4**2)
    directory = './../application_examples/harmonic_potential_well/'
    file = 'energy.ref'
    np.savetxt(os.path.join(directory, file), eig_val)


def _eigenvalue_harmonic_oscillator():
    """Calculates the energy eigenvalues of the harmonic oscillator."""
    eig_val = np.ones((5, ), dtype=float)
    for ii in range(0, 5):
        eig_val[ii] = 0.5*(ii + 0.5)
    directory = './../application_examples/harmonic_potential_well/'
    file = 'energy.ref'
    np.savetxt(os.path.join(directory, file), eig_val)
