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



def z(x1, x2, funcion):
    """
    Calcula el siguiente punto de aproximación en el método de la secante.
    
    :Example:
    
    >>> def funcion(x):
    ...     return x**2 - 4
    >>> x1, x2 = 1.0, 3.0
    >>> z(x1, x2, funcion)
    2.090909090909091
    
    :param x1: Primer punto de evaluación.
    :type x1: float
    :param x2: Segundo punto de evaluación.
    :type x2: float
    :param funcion: La función objetivo.
    :type funcion: callable
    :return: El siguiente punto de aproximación.
    :rtype: float
    """
    parte_arriba = primera_derivada(x2,funcion)

    primera_parte = (primera_derivada(x2,funcion)) - (primera_derivada(x1,funcion))
    segunda_parte = x2 - x1
    parte_abajo = primera_parte/segunda_parte
    
    parte_final = parte_arriba / parte_abajo
    resul = x2 - parte_final
    return resul






def metodo_secante(x_inicial, funcion, epsilon, iter_max=100):
    """
    Encuentra una raíz de una función no lineal usando el método de la secante.
    El método de la secante es un algoritmo numérico iterativo para encontrar 
    las raíces de una función no lineal. A diferencia del método de Newton-Raphson, 
    no requiere la evaluación de la derivada de la función en cada paso, haciendo 
    el cálculo de la derivada menos crítico.

    :Example:

    >>> def funcion(x):
    ...     return x**3 - x - 2
    >>> x_inicial = (1.0, 2.0)
    >>> epsilon = 1e-6
    >>> metodo_secante(x_inicial, funcion, epsilon)
    1.5213797068045676

    :param x_inicial: Tupla con los dos puntos iniciales para comenzar el método.
    :type x_inicial: tuple
    :param funcion: Función objetivo.
    :type funcion: callable
    :param epsilon: Tolerancia para la convergencia del método.
    :type epsilon: float
    :param iter_max: Número máximo de iteraciones permitidas. Default es 100.
    :type iter_max: int, optional
    :return: Aproximación de la raíz encontrada.
    :rtype: float
    :raises: ValueError si el método no converge después de iter_max iteraciones.
    """

    x1 = x_inicial[0]
    x2 = x_inicial[1]
    
    iteracion = 0
    while abs(x1 - x2) > epsilon and iteracion < iter_max:
        x_nuevo = z(x1, x2, funcion)
        x1 = x2
        x2 = x_nuevo
        iteracion += 1
    
    if iteracion == iter_max:
        print("El método de la secante no convergió después de", iter_max, "iteraciones.")
    
    return x2

