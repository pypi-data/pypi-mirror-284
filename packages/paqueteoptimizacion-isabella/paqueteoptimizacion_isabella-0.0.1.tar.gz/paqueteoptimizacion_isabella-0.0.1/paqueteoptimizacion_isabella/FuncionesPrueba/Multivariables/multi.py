import numpy as np
import math

def prueba(x):
    """
    Calcula la suma de los cuadrados de los elementos de x.

    :Ejemplo:

    >>> prueba(np.array([1, 2, 3]))
    14

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Suma de los cuadrados de los elementos de x.
    :rtype: float
    """
    return np.sum(np.square(x))


def Rastrigin(x):
    """
    Calcula la función Rastrigin, una función común de prueba en la optimización global.

    :Ejemplo:

    >>> Rastrigin(np.array([1, 2, 3]))
    29.0

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función Rastrigin.
    :rtype: float
    """
    n = len(x)
    return 10 * n + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))


def ackley_function(x):
    """
    Calcula la función Ackley, una función común de prueba en la optimización global.

    :Ejemplo:

    >>> ackley_function(np.array([1, 2, 3]))
    11.59615047203264

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función Ackley.
    :rtype: float
    """
    n = len(x)
    term1 = -20 * np.exp(-0.2 * np.sqrt(np.sum(x**2) / n))
    term2 = -np.exp(np.sum(np.cos(2 * np.pi * x)) / n)
    return term1 + term2 + np.e + 20


def sphere_function(x):
    """
    Calcula la función esfera, que es la suma de los cuadrados de los elementos de x.

    :Ejemplo:

    >>> sphere_function(np.array([1, 2, 3]))
    14

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Suma de los cuadrados de los elementos de x.
    :rtype: float
    """
    return np.sum(x**2)


def Rosenbrock(x):
    """
    Calcula la función Rosenbrock, una función común de prueba en la optimización global.

    :Ejemplo:

    >>> Rosenbrock(np.array([1, 2, 3]))
    402

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función Rosenbrock.
    :rtype: float
    """
    return np.sum(100 * (x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)


def beale_function(x):
    """
    Calcula la función Beale, que es solo para vectores de dimensión 2.

    :Ejemplo:

    >>> beale_function(np.array([1, 2]))
    7.203125

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función Beale.
    :rtype: float
    :raises ValueError: Si el vector no es de dimensión 2.
    """
    if len(x) != 2:
        raise ValueError("La función Beale sólo acepta un vector de dimensión 2.")
    return (1.5 - x[0] + x[0]*x[1])**2 + (2.25 - x[0] + x[0]*x[1]**2)**2 + (2.625 - x[0] + x[0]*x[1]**3)**2


def goldstein_price_function(x):
    """
    Calcula la función Goldstein-Price, que es solo para vectores de dimensión 2.

    :Ejemplo:

    >>> goldstein_price_function(np.array([1, 2]))
    15566

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función Goldstein-Price.
    :rtype: float
    :raises ValueError: Si el vector no es de dimensión 2.
    """
    if len(x) != 2:
        raise ValueError("La función Goldstein-Price sólo acepta un vector de dimensión 2.")
    x1, x2 = x
    part1 = 1 + (x1 + x2 + 1)**2 * (19 - 14*x1 + 3*x1**2 - 14*x2 + 6*x1*x2 + 3*x2**2)
    part2 = 30 + (2*x1 - 3*x2)**2 * (18 - 32*x1 + 12*x1**2 + 48*x2 - 36*x1*x2 + 27*x2**2)
    return part1 * part2


def booth_function(x):
    """
    Calcula la función Booth, que es solo para vectores de dimensión 2.

    :Ejemplo:

    >>> booth_function(np.array([1, 2]))
    74

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función Booth.
    :rtype: float
    :raises ValueError: Si el vector no es de dimensión 2.
    """
    if len(x) != 2:
        raise ValueError("La función Booth sólo acepta un vector de dimensión 2.")
    return (x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2


def bukin_function(x):
    """
    Calcula la función Bukin, que es solo para vectores de dimensión 2.

    :Ejemplo:

    >>> bukin_function(np.array([1, 2]))
    100.03

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función Bukin.
    :rtype: float
    :raises ValueError: Si el vector no es de dimensión 2.
    """
    if len(x) != 2:
        raise ValueError("La función Bukin sólo acepta un vector de dimensión 2.")
    return 100 * np.sqrt(np.abs(x[1] - 0.01 * x[0]**2)) + 0.01 * np.abs(x[0] + 10)


def matyas_function(x):
    """
    Calcula la función Matyas, que es solo para vectores de dimensión 2.

    :Ejemplo:

    >>> matyas_function(np.array([1, 2]))
    1.36

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función Matyas.
    :rtype: float
    :raises ValueError: Si el vector no es de dimensión 2.
    """
    if len(x) != 2:
        raise ValueError("La función Matyas sólo acepta un vector de dimensión 2.")
    return 0.26 * (x[0]**2 + x[1]**2) - 0.48 * x[0] * x[1]


def levi_function(x):
    """
    Calcula la función Levi, que es solo para vectores de dimensión 2.

    :Ejemplo:

    >>> levi_function(np.array([1, 2]))
    9.25000404192189

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función Levi.
    :rtype: float
    :raises ValueError: Si el vector no es de dimensión 2.
    """
    if len(x) != 2:
        raise ValueError("La función Levi sólo acepta un vector de dimensión 2.")
    return np.sin(3 * np.pi * x[0])**2 + (x[0] - 1)**2 * (1 + np.sin(3 * np.pi * x[1])**2) + (x[1] - 1)**2 * (1 + np.sin(2 * np.pi * x[1])**2)


def himmelblaus(x):
    """
    Calcula la función Himmelblau, que es solo para vectores de dimensión 2.

    :Ejemplo:

    >>> himmelblaus(np.array([1, 2]))
    136

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función Himmelblau.
    :rtype: float
    :raises ValueError: Si el vector no es de dimensión 2.
    """
    if len(x) != 2:
        raise ValueError("La función Himmelblau sólo acepta un vector de dimensión 2.")
    return (x[0]**2 + x[1] - 11)**2 + (x[0] + x[1]**2 - 7)**2


def threehump_camel_function(x):
    """
    Calcula la función Three-hump Camel, que es solo para vectores de dimensión 2.

    :Ejemplo:

    >>> threehump_camel_function(np.array([1, 2]))
    2.8055555555555554

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función Three-hump Camel.
    :rtype: float
    :raises ValueError: Si el vector no es de dimensión 2.
    """
    if len(x) != 2:
        raise ValueError("La función Three-hump Camel sólo acepta un vector de dimensión 2.")
    return 2 * x[0]**2 - 1.05 * x[0]**4 + (x[0]**6) / 6 + x[0] * x[1] + x[1]**2


def easom_function(x):
    """
    Calcula la función Easom, que es solo para vectores de dimensión 2.

    :Ejemplo:

    >>> easom_function(np.array([1, 2]))
    -5.450263760955594e-06

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función Easom.
    :rtype: float
    :raises ValueError: Si el vector no es de dimensión 2.
    """
    if len(x) != 2:
        raise ValueError("La función Easom sólo acepta un vector de dimensión 2.")
    return -np.cos(x[0]) * np.cos(x[1]) * np.exp(-((x[0] - np.pi)**2 + (x[1] - np.pi)**2))


def cross_in_tray_function(x):
    """
    Calcula la función Cross-in-Tray, que es solo para vectores de dimensión 2.

    :Ejemplo:

    >>> cross_in_tray_function(np.array([1, 2]))
    -0.000217456657078836

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función Cross-in-Tray.
    :rtype: float
    :raises ValueError: Si el vector no es de dimensión 2.
    """
    if len(x) != 2:
        raise ValueError("La función Cross-in-Tray sólo acepta un vector de dimensión 2.")
    return -0.0001 * (np.abs(np.sin(x[0]) * np.sin(x[1]) * np.exp(np.abs(100 - np.sqrt(x[0]**2 + x[1]**2) / np.pi))) + 1)**0.1


def eggholder(x):
    """
    Calcula la función Eggholder, que es solo para vectores de dimensión 2.

    :Ejemplo:

    >>> eggholder(np.array([1, 2]))
    -25.841535694421856

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función Eggholder.
    :rtype: float
    :raises ValueError: Si el vector no es de dimensión 2.
    """
    if len(x) != 2:
        raise ValueError("La función Eggholder sólo acepta un vector de dimensión 2.")
    return -(x[1] + 47) * np.sin(np.sqrt(np.abs(x[0]/2 + (x[1] + 47)))) - x[0] * np.sin(np.sqrt(np.abs(x[0] - (x[1] + 47))))


def holder_table(x):
    """
    Calcula la función Holder Table, que es solo para vectores de dimensión 2.

    :Ejemplo:

    >>> holder_table(np.array([1, 2]))
    -1.0352761804100832

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función Holder Table.
    :rtype: float
    :raises ValueError: Si el vector no es de dimensión 2.
    """
    if len(x) != 2:
        raise ValueError("La función Holder Table sólo acepta un vector de dimensión 2.")
    return -np.abs(np.sin(x[0]) * np.cos(x[1]) * np.exp(np.abs(1 - np.sqrt(x[0]**2 + x[1]**2) / np.pi)))


def mccormick(x):
    """
    Calcula la función McCormick, que es solo para vectores de dimensión 2.

    :Ejemplo:

    >>> mccormick(np.array([1, 2]))
    3.197415370720147

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función McCormick.
    :rtype: float
    :raises ValueError: Si el vector no es de dimensión 2.
    """
    if len(x) != 2:
        raise ValueError("La función McCormick sólo acepta un vector de dimensión 2.")
    return np.sin(x[0] + x[1]) + (x[0] - x[1])**2 - 1.5 * x[0] + 2.5 * x[1] + 1


def schaffer_function_n2(x):
    """
    Calcula la función Schaffer N. 2, que es solo para vectores de dimensión 2.

    :Ejemplo:

    >>> schaffer_function_n2(np.array([1, 2]))
    0.01263557920118913

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función Schaffer N. 2.
    :rtype: float
    :raises ValueError: Si el vector no es de dimensión 2.
    """
    if len(x) != 2:
        raise ValueError("La función Schaffer N. 2 sólo acepta un vector de dimensión 2.")
    return 0.5 + (np.sin(x[0]**2 - x[1]**2)**2 - 0.5) / (1 + 0.001 * (x[0]**2 + x[1]**2))**2


def schaffer_function_n4(x):
    """
    Calcula la función Schaffer N. 4, que es solo para vectores de dimensión 2.

    :Ejemplo:

    >>> schaffer_function_n4(np.array([1, 2]))
    0.014689956223166331

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función Schaffer N. 4.
    :rtype: float
    :raises ValueError: Si el vector no es de dimensión 2.
    """
    if len(x) != 2:
        raise ValueError("La función Schaffer N. 4 sólo acepta un vector de dimensión 2.")
    return 0.5 + (np.cos(np.sin(np.abs(x[0]**2 - x[1]**2)))**2 - 0.5) / (1 + 0.001 * (x[0]**2 + x[1]**2))**2


def styblinski_tang_2d(x):
    """
    Calcula la función Styblinski-Tang, que es solo para vectores de dimensión 2.

    :Ejemplo:

    >>> styblinski_tang_2d(np.array([1, 2]))
    -16.25

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :return: Valor de la función Styblinski-Tang.
    :rtype: float
    :raises ValueError: Si el vector no es de dimensión 2.
    """
    if len(x) != 2:
        raise ValueError("La función Styblinski-Tang sólo acepta un vector de dimensión 2.")
    return (x[0]**4 - 16 * x[0]**2 + 5 * x[0] + x[1]**4 - 16 * x[1]**2 + 5 * x[1]) / 2


def shekel_function(x, C, beta):
    """
    Calcula la función Shekel, que es solo para vectores de dimensión 2.

    :Ejemplo:

    >>> C = np.array([[0.5, 0.5], [0.1, 0.9], [0.2, 0.8]])
    >>> beta = np.array([0.1, 0.2, 0.3])
    >>> shekel_function(np.array([1, 2]), C, beta)
    -0.44567773022905644

    :param x: Array de variables de entrada.
    :type x: numpy.ndarray
    :param C: Matriz de coeficientes.
    :type C: numpy.ndarray
    :param beta: Vector de coeficientes.
    :type beta: numpy.ndarray
    :return: Valor de la función Shekel.
    :rtype: float
    :raises ValueError: Si el vector no es de dimensión 2.
    """
    if len(x) != 2:
        raise ValueError("La función Shekel sólo acepta un vector de dimensión 2.")
    return -np.sum(1.0 / (np.sum((x - C)**2, axis=1) + beta))
