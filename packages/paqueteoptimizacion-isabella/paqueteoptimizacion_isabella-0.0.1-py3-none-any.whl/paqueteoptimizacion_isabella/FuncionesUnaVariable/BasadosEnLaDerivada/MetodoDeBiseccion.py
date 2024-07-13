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

def metodo_biseccion(x, funcion, epsilon):
    """
    Encuentra una raíz de una función usando el método de bisección.
    El método de bisección es un algoritmo numérico para encontrar 
    raíces de una función en un intervalo dado. Funciona dividiendo 
    repetidamente el intervalo por la mitad y seleccionando el subintervalo 
    donde la raíz probablemente se encuentra, hasta que el intervalo sea lo 
    suficientemente pequeño o se alcance una precisión especificada.

    :Example:

    >>> def funcion(x):
    ...     return x**3 - x - 2
    >>> x = (-2, 2)
    >>> epsilon = 1e-6
    >>> metodo_biseccion(x, funcion, epsilon)
    1.5213797092437744

    :param x: Intervalo inicial [a, b] donde se busca la raíz.
    :type x: tuple
    :param funcion: Función objetivo.
    :type funcion: callable
    :param epsilon: Tolerancia para la convergencia del método.
    :type epsilon: float
    :return: Aproximación de la raíz encontrada.
    :rtype: float
    """

    a_original = x[0]
    b_original = x[-1]

    puntos_prueba = np.arange(a_original, b_original, 0.1)
    
    a = next(p for p in puntos_prueba if primera_derivada(p, funcion) <= 0)
    b = next(p for p in puntos_prueba if segunda_derivada(p, funcion) >= 0)
    
    x1 = a
    x2 = b
    
    
    z = (x2 + x1) / 2
    while abs(x1 - x2) > epsilon:
        z = (x2 + x1) / 2
        if primera_derivada(z, funcion) < 0:
            x1 = z
        elif primera_derivada(z, funcion) > 0:
            x2 = z
    
    return z




