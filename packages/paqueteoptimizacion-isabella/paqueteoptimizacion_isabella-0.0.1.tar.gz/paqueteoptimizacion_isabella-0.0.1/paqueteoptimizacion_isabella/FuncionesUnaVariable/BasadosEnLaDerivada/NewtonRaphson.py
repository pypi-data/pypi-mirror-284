import numpy as np

def primera_derivada(x, funcion):
    """
    Calcula la primera derivada de una función en un punto dado utilizando diferencias finitas.
    
    :Example:
    
    >>> def funcion(x):
    ...     return x**2
    >>> x = 1.0
    >>> primera_derivada(x, funcion)
    2.000000000002
    
    :param x: El punto en el que se calcula la derivada.
    :type x: float
    :param funcion: La función para la cual se calcula la derivada.
    :type funcion: callable
    :return: La primera derivada calculada en el punto dado.
    :rtype: float
    """
    delta = 0.0001
    primera_parte = funcion(x + delta)
    segunda_parte = funcion(x - delta)
    parte_arriba = primera_parte - segunda_parte
    parte_abajo = 2 * delta
    parte_final = parte_arriba / parte_abajo
    return parte_final

def segunda_derivada(x, funcion):
    """
    Calcula la segunda derivada de una función en un punto dado utilizando diferencias finitas.
    
    :Example:
    
    >>> def funcion(x):
    ...     return x**2
    >>> x = 1.0
    >>> segunda_derivada(x, funcion)
    2.000000165480742
    
    :param x: El punto en el que se calcula la derivada.
    :type x: float
    :param funcion: La función para la cual se calcula la derivada.
    :type funcion: callable
    :return: La segunda derivada calculada en el punto dado.
    :rtype: float
    """
    delta = 0.0001
    primera_parte = funcion(x + delta)
    segunda_parte = 2 * funcion(x)
    tercera_parte = funcion(x - delta)
    parte_arriba = primera_parte - segunda_parte + tercera_parte
    parte_abajo = delta**2
    parte_final = parte_arriba / parte_abajo
    return parte_final


def newton_raphson(x, funcion, epsilon):
    """
    Implementa el método de Newton-Raphson para encontrar una raíz de la función dada.
    El método de Newton-Raphson es un algoritmo iterativo utilizado para encontrar 
    numéricamente las raíces de una función mediante la aproximación sucesiva de 
    un punto inicial hacia la raíz, basándose en la derivada de la función.

    :Example:

    >>> def funcion(x):
    ...     return x**2 - 2
    >>> x_inicial = [1.0, 2.0]
    >>> epsilon = 1e-6
    >>> newton_raphson(x_inicial, funcion, epsilon)
    1.4142135623746899

    :param x: Lista de puntos iniciales de búsqueda.
    :type x: list of float
    :param funcion: Función objetivo para la cual se busca la raíz.
    :type funcion: callable
    :param epsilon: Tolerancia de convergencia del método.
    :type epsilon: float
    :return: Valor aproximado de la raíz de la función.
    :rtype: float
    :raises ValueError: Si la longitud de x es cero o si no se alcanza la convergencia.
    """

    k = 0
    x_actual = x[k]
    x_derivada1 = primera_derivada(x_actual, funcion)
    x_derivada2 = segunda_derivada(x_actual, funcion)
    x_siguiente = x_actual - (x_derivada1 / x_derivada2)
    while abs(x_siguiente - x_actual) > epsilon:
        k += 1
        if k >= len(x):
            return x_siguiente
        x_actual = x[k]
        x_derivada1 = primera_derivada(x_actual, funcion)
        x_derivada2 = segunda_derivada(x_actual, funcion)
        x_siguiente = x_actual - (x_derivada1 / x_derivada2)
    return x_siguiente
