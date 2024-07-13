import math

def regla_eliminacion(x1, x2, fx1, fx2, a, b):
    """
    Regla de eliminación utilizada en la búsqueda dorada.

    Parameters:
    x1 (float): Primer punto de comparación.
    x2 (float): Segundo punto de comparación.
    fx1 (float): Valor de la función en x1.
    fx2 (float): Valor de la función en x2.
    a (float): Límite inferior del intervalo de búsqueda.
    b (float): Límite superior del intervalo de búsqueda.

    Returns:
    tuple: Nuevo intervalo de búsqueda (a, b).
    """
    if fx1 > fx2:
        return x1, b
    if fx1 < fx2:
        return a, x2
    return x1, x2

def w_to_x(w, a, b):
    """
    Convierte un punto w en el intervalo [0, 1] al intervalo [a, b].

    Parameters:
    w (float): Punto en el intervalo [0, 1].
    a (float): Límite inferior del intervalo de búsqueda.
    b (float): Límite superior del intervalo de búsqueda.

    Returns:
    float: Punto convertido en el intervalo [a, b].
    """
    return w * (b - a) + a

def busqueda_dorada(funcion, epsilon, a, b):
    """
    Implementación del método de búsqueda por la razón áurea (Golden Section Search) para minimización de funciones.

    Usa todas las capacidades de Sphinx en esta descripción, por ejemplo, para dar
    ejemplos de uso ...

    :Ejemplo:

    >>> busqueda_dorada(lambda x: x**2, 0.01, -1, 1)
    0.0

    :param funcion: Función objetivo que se desea minimizar.
    :type funcion: callable
    :param epsilon: Precisión deseada para la aproximación del mínimo.
    :type epsilon: float
    :param a: Límite inferior del intervalo de búsqueda.
    :type a: float
    :param b: Límite superior del intervalo de búsqueda.
    :type b: float
    :return: Punto donde se estima que se encuentra el mínimo de la función.
    :rtype: float
    :raises ValueError: Si el intervalo no está correctamente definido.
    """

    PHI = (1 + math.sqrt(5)) / 2 - 1
    aw, bw = 0, 1
    Lw = 1
    k = 1
    while Lw > epsilon:
        w2 = aw + PHI * Lw
        w1 = bw - PHI * Lw
        aw, bw = regla_eliminacion(w1, w2, funcion(w_to_x(w1, a, b)), funcion(w_to_x(w2, a, b)), aw, bw)
        k += 1
        Lw = bw - aw
    return (w_to_x(aw, a, b) + w_to_x(bw, a, b)) / 2
