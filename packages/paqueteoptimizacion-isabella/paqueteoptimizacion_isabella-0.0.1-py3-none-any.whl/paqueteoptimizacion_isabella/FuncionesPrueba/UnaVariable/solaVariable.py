import math
import numpy as np

def lata(x):
    """
    Calcula la operación para una lata cilíndrica dada una variable x.

    Usa todas las capacidades de Sphinx en esta descripción, por ejemplo, para dar
    ejemplos de uso ...

    :Ejemplo:

    >>> lata(np.array([5]))
    array([162.83185307])

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Resultado de la operación ((2 * π) * (x^2) + 500/x).
    :rtype: numpy.ndarray
    :raises ValueError: Si algún elemento de x es cero.
    """
    operacion = ((2 * np.pi) * (x**2) + 500/x)
    return operacion

def caja(x):
    """
    Calcula el volumen de una caja con dimensiones dependientes de x.

    Usa todas las capacidades de Sphinx en esta descripción, por ejemplo, para dar
    ejemplos de uso ...

    :Ejemplo:

    >>> caja(np.array([2]))
    array([-288])

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Volumen de la caja.
    :rtype: numpy.ndarray
    :raises ValueError: Si algún elemento de x hace que las dimensiones de la caja sean no positivas.
    """
    return -1 * (((20 - (2 * x)) * (10 - (2 * x))) * (x))

def funcion1(x):
    """
    Calcula la función f(x) = x^2 + 54/x.

    Usa todas las capacidades de Sphinx en esta descripción, por ejemplo, para dar
    ejemplos de uso ...

    :Ejemplo:

    >>> funcion1(np.array([3]))
    array([29.18])

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Resultado de la función.
    :rtype: numpy.ndarray
    :raises ValueError: Si algún elemento de x es cero.
    """
    return (x**2) + (54/x)

def funcion2(x):
    """
    Calcula la función f(x) = x^3 + 2x - 3.

    Usa todas las capacidades de Sphinx en esta descripción, por ejemplo, para dar
    ejemplos de uso ...

    :Ejemplo:

    >>> funcion2(np.array([1]))
    array([0.0])

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Resultado de la función.
    :rtype: numpy.ndarray
    """
    return (x**3) + (2*x) - 3

def funcion3(x):
    """
    Calcula la función f(x) = x^4 + x^2 - 33.

    Usa todas las capacidades de Sphinx en esta descripción, por ejemplo, para dar
    ejemplos de uso ...

    :Ejemplo:

    >>> funcion3(np.array([2]))
    array([-25])

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Resultado de la función.
    :rtype: numpy.ndarray
    """
    return (x**4) + (x**2) - 33

def funcion4(x):
    """
    Calcula la función f(x) = 3x^4 - 8x^3 - 6x^2 + 12x.

    Usa todas las capacidades de Sphinx en esta descripción, por ejemplo, para dar
    ejemplos de uso ...

    :Ejemplo:

    >>> funcion4(np.array([1]))
    array([-5])

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Resultado de la función.
    :rtype: numpy.ndarray
    """
    return (3 * (x**4)) - (8 * (x**3)) - (6 * (x**2)) + (12 * x)
