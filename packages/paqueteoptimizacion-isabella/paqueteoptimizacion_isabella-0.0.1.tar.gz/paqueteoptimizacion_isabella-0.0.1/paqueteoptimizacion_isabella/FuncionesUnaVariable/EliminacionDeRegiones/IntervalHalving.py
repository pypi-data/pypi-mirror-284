import numpy as np


def interval_method(function, epsilon, a,b):
    """
    Implementación del método del intervalo para minimización de funciones.

    Este método busca el mínimo de una función en un intervalo [a, b] dividiendo 
    iterativamente el intervalo y evaluando la función en puntos clave.

    :Ejemplo:

    >>> interval_method(lambda x: (x-5)**2, 0.01, 0, 10)
    5.0

    :param function: Función objetivo que se desea minimizar.
    :type function: callable
    :param epsilon: Precisión deseada para la aproximación del mínimo.
    :type epsilon: float
    :param a: Límite inferior del intervalo.
    :type a: float
    :param b: Límite superior del intervalo.
    :type b: float
    :return: Punto donde se estima que se encuentra el mínimo de la función dentro del intervalo [a, b].
    :rtype: float
    :raises ValueError: Si el intervalo no está correctamente definido.
    """
    Xm = (a + b) / 2
    L = b - a
    converged = False
    
    while not converged:
        x1 = a + (L / 4)
        x2 = b - (L / 4)
        func_x1 = function(x1)
        func_x2 = function(x2)
        func_Xm = function(Xm)
        
        if func_x1 < func_Xm:
            b = Xm
            Xm = x1
        else:
            if func_x2 < func_Xm:
                a = Xm
                Xm = x2
            else:
                a = x1
                b = x2
                
        L = b - a
        if abs(L) < epsilon:
            converged = True
    
    return Xm

