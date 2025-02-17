from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from math import exp
from math import cos
from math import sin


def circle_evaluate(t, r, z=0):
    """Evalutes a circle at a parameter.

    Parameters
    ----------
    t: float
        Parameter.
    r: float
        Radius of the circle.
    z: float, optional
        Elevation of the circle above the XY plane.

    Returns
    -------
    [float, float, float]
        The XYZ coordinates.

    """
    return [r * cos(t), r * sin(t), z]


def ellipse_evaluate(t, a, b, z=0):
    """Evalutes an ellipse at a parameter.

    Parameters
    ----------
    t: float
        Parameter.
    a: float
        Ellipse major.
    b: float
        Ellipse minor.
    z: float, optional
        Elevation of the ellipse above the XY plane.

    Notes
    -----
    The radius along the x and y axes are a and b, respectively.

    Returns
    -------
    [float, float, float]
        The XYZ coordinates.

    """
    return [a * cos(t), b * sin(t), z]


def archimedean_spiral_evaluate(t, a, b, z=0):
    """Evalutes a spiral at a parameter.

    The analytical polar equation is r = a + b * theta.

    Parameters
    ----------
    t: float
        Parameter.
    a: float
        The angle of the tangent at the beginning is equal to a.
    b: float
        The radius between turns is equal to 2 * pi * b.
    z: float, optional
        Elevation of the spiral segment above the XY plane.

    Returns
    -------
    [float, float, float]
        The XYZ coordinates.

    References
    ----------
    * GeoGebra. *Archimedean Spiral built by parametric equations*. Available at: https://www.geogebra.org/m/dZuH5hWa.

    """
    return [b * t * cos(t + a), b * t * sin(t + a), z]


def logarithmic_spiral_evaluate(t, a, b, z=0):
    """Evalutes a logarithmic spiral at a parameter.

    The analytical polar equation is r = a * exp(b * theta).

    Parameters
    ----------
    t: float
        Parameter.
    a: float
        The angle of the tangent at the beginning is equal to a.
    b: float
        The radius between turns is equal to 2 * pi * b.
    z: float, optional
        Elevation of the spiral segment above the XY plane.

    Returns
    -------
    [float, float, float]
        The XYZ coordinates.

    References
    ----------
    * GeoGebra. *An equiangular spiral - parametric equation*. Available at: https://www.geogebra.org/m/zsHgCvq7.

    """
    return [a * exp(b * t) * cos(t), a * exp(b * t) * sin(t), z]


def helix_evaluate(t, a, b):
    """Evalutes an helix at a parameter.

    Parameters
    ----------
    t: float
        Parameter.
    a: float
        The radius of the helix is a.
    b: float
        The slope of the helix is b / a.

    Returns
    -------
    [float, float, float]
        The XYZ coordinates.

    Notes
    -----
    An interpretation of the constants a and b are the radius of the helix is a, and the slope of the helix is b / a.

    References
    ----------
    .. [1] Wolfram MathWorld. *Helix*.
               Available at: http://mathworld.wolfram.com/Helix.html.
    """
    return [a * cos(t), a * sin(t), b * t]
