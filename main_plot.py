#!/usr/bin/env python3
"""Main program for plotting the calculated data"""


from modules import plot


def main():

    isdir = plot.check_dir()

    direc, lim_x, lim_y, eigenlim, scalefac, unclim_x = plot.user_inp(isdir)
    x_val, potential, eigenfunctions, energies, expec_val, uncertainties = plot.readplotdata(direc)

    plot.display_plots(x_val, potential, eigenfunctions, energies, expec_val,
                       lim_x, lim_y, eigenlim, scalefac, uncertainties,
                       unclim_x)


if __name__ == "__main__":
    main()
