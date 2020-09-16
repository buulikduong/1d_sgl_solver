"""
Pytest functions for testing potentials and eigenvalues of
application examples. Calculations of reference potential for both potential
square wells and for the harmonic oscillator are based on known analytic
solution. Calculations of reference eigenvalues for infinite square well and
the harmonic oscillator are based on known analytic solution. Other reference
files were numerically calculated.
"""
import numpy as np
import pytest
import modules

EXAMPLES = ['infinite_potential_well', 'finite_potential_well',
            'double_linear', 'harmonic_potential_well', 'double_cubic_spline',
            'asym_potential_well']


@pytest.mark.parametrize("example", EXAMPLES)
def test_potential(example):
    """
    Tests if computet potentials match the reference potentials.
    """
    path = "./application_examples/{}/".format(example)
    ref_potential = np.loadtxt(path + "potential.ref")
    parameter = modules.in_and_out.read_inp(path)
    intfunc = modules.interpolator.interpolator(parameter['x_decl'],
                                                parameter['y_decl'],
                                                parameter['interpol_method'])
    x_points = np.linspace(parameter['xMin'],
                           parameter['xMax'],
                           parameter['nPoint'])
    potential_test = [intfunc(ii) for ii in x_points]
    assert np.all(ref_potential - potential_test < 1e-15)


@pytest.mark.parametrize("example", EXAMPLES)
def test_energy(example):
    """
    Tests if computet energys match the reference energy eigenvalues.
    """
    path = "./application_examples/{}/".format(example)
    ref_energy = np.loadtxt(path + "energy.ref")
    energy_test = np.loadtxt(path + "energies.dat")
    if example[0] == 'infinite_potential_well':
        assert np.allclose(ref_energy, test_energy, rtol=1e-02, atol=1e-12)
    elif example[0] == 'harmonic_potential_well':
        assert np.allclose(ref_energy, energy_test, rtol=1e-03, atol=1e-12)
    else:
        assert np.allclose(ref_energy, energy_test)
