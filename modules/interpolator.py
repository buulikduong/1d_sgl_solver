"""Module interpolating mathematical functions out of support points"""

from scipy.interpolate import interp1d, lagrange, CubicSpline


def interpolator(x_sup, y_sup, method):
    """Interpolates a mathematical function from a given set of
    points using either linear, polynomial or cubic spline for the
    interpolation.

    Args:
        x_sup (list): x-coordinates of the function
        y_sup (list): y-coordinates of the function
        method (string): name of the interpolation method to be used

    Returns:
        intfunc: interpolated function
    """

    if method == "linear":
        intfunc = interp1d(x_sup, y_sup, kind="linear")
        return intfunc
    elif method == "polynomial":
        intfunc = lagrange(x_sup, y_sup)
        return intfunc
    elif method == "cspline":
        intfunc = CubicSpline(x_sup, y_sup, bc_type="natural")
        return intfunc
