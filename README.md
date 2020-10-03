# 1d stationary schrodinger equation solver

## Purpose

This program solves the 1 dimensional stationary schrodinger
equation for a freely selectable area on an interpolated
potential. It returns the energy-eigenvalues, wavefunctions,
expectation values and the uncertainty of position x. In
addition the potential, eigenvalues and their corresponding
wavefunctions (and expcetation values) are vizualized.

## Requirements

The program needs Python 3.6 (or higher)
and the packages numpy, scipy, matplotlib, os.

## Executing program

For executing program the input file should be named 'schrodinger.inp' and
must in the form:

```python
-2.0 2.0 1999   # xMin xMax nPoint
1 5             # first and last eigenvalue to print
linear          # interpolation type
2               # nr. of interpolation points and xy declarations
-2.0 0.0
 2.0 0.0
```
It is necessary that all physical quantities are given in atomic units.
The unit of the energy will be Hartree and the unit for the lenght will be
calculated in Bohr.

For showing the help page with the description of the script and its arguments,
please enter following line into your unix shell:

```bash
python3 main_solver -h
```

For visualizing the saved output data, please execute the script `main_plot`
either in your unix shell or in your IDE (for example Spyder).\n
Some plot-parameters can be set by the user, for example:

```bash
Please input the range of the x-axis as a tuple:
```

A valid answer/input should be entered in the form:

```bash
-2, 2
```

If default-settings are prefered, just press ENTER without any inputs.\n
The plots will be shown on screen and then can be saved manually by the user
in a prefered file format (f.e. as a PDF or PNG).

## Modules

To get information of the modules containing the main functionality
of this solver, please read the API documentation. Access to the API
documentation can be obtained by:

* i)    Switch to the directory `1d_sgl_solver/docs`
* ii)   Enter `make html`
* iii)  Enter `firefox _build/html/index.html`

Note: If you do not use firefox, other browsers work as well.

## Authors/Contact

Buu Lik Duong (buulik@uni-bremen.de)
Jarik Bahrenburg (jarik@uni-bremen.de)

## Version History

0.1: Initial release

## License

Please see the LICENSE.txt file for details.

## Further notes

This is a student project.

