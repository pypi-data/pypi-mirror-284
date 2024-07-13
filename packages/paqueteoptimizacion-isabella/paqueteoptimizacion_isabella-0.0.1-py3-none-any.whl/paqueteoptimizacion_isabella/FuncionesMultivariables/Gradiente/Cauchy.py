import numpy as np
import math



# ---------------------------------- GRADIENTE ---------------------------------- 
def gradiente(funcion, x, delta=0.001):
    """
    Calcula el gradiente de una función en un punto dado utilizando diferencias finitas.

    :Example:

    >>> def funcion(x):
    ...     return sum(xi**2 for xi in x)
    >>> x = np.array([1.0, 2.0])
    >>> gradiente(funcion, x)
    array([2.001, 4.001])

    :param funcion: La función objetivo cuya derivada se desea calcular.
    :type funcion: callable
    :param x: El punto en el que se desea calcular el gradiente.
    :type x: ndarray
    :param delta: El tamaño del paso para calcular las diferencias finitas. Default es 0.001.
    :type delta: float, optional
    :return: El gradiente calculado en el punto dado.
    :rtype: ndarray
    """
    derivadas = []
    for i in range(len(x)):
        copia = x.copy()
        copia[i] = x[i] + delta
        valor1 = funcion(copia)
        copia[i] = x[i] - delta
        valor2 = funcion(copia)
        derivada = (valor1 - valor2) / (2 * delta)
        derivadas.append(derivada)
    return np.array(derivadas)





# ----------------------------------- DISTANCIA ORIGEN ----------------------------------
def distancia_origen(vector):
    """
    Calcula la distancia euclidiana de un vector al origen.

    :Example:

    >>> vector = np.array([3.0, 4.0])
    >>> distancia_origen(vector)
    5.0

    :param vector: El vector cuya distancia al origen se desea calcular.
    :type vector: ndarray
    :return: La distancia euclidiana del vector al origen.
    :rtype: float
    """
    return np.linalg.norm(vector)







# --------------------------------------- CAUCHY -------------------------------------
def cauchy(funcion_objetivo, x, metodo_busqueda, epsilon1=1e-6, epsilon2=1e-6, max_iterations=100):
    """
    Implementa el método de Cauchy para la optimización de funciones con restricciones.
    El Método de Cauchy, también conocido como el método del gradiente descendente, 
    es una técnica de optimización iterativa utilizada para encontrar el mínimo de una función.

    :Example:

    >>> def funcion_objetivo(x):
    ...     return sum(xi**2 for xi in x)
    >>> def metodo_busqueda(alpha_calcular, epsilon, a, b):
    ...     return 0.1  # Dummy implementation for example
    >>> x = np.array([1.0, 1.0])
    >>> cauchy(funcion_objetivo, x, metodo_busqueda)
    array([0., 0.])

    :param funcion_objetivo: La función objetivo a minimizar.
    :type funcion_objetivo: callable
    :param x: Punto inicial de búsqueda.
    :type x: ndarray
    :param metodo_busqueda: Método de búsqueda para calcular el paso alpha.
    :type metodo_busqueda: callable
    :param epsilon1: Tolerancia para la condición de convergencia basada en la distancia del gradiente al origen. Default es 1e-6.
    :type epsilon1: float, optional
    :param epsilon2: Tolerancia para la condición de convergencia basada en la diferencia relativa entre iteraciones. Default es 1e-6.
    :type epsilon2: float, optional
    :param max_iterations: Número máximo de iteraciones permitidas. Default es 100.
    :type max_iterations: int, optional
    :return: Punto óptimo encontrado.
    :rtype: ndarray
    """

    terminar = False
    xk = x
    k = 0
    while not terminar:
        gradienteX = np.array(gradiente(funcion_objetivo,xk))
        distancia = distancia_origen(gradienteX)
        if distancia <= epsilon1:
            terminar = True
        elif (k >= max_iterations):
            terminar = True
        else:
            def alpha_calcular(alpha):
                return funcion_objetivo(xk - alpha*gradienteX)
            alpha = metodo_busqueda(alpha_calcular,epsilon2, 0.0,1.0)
            x_k1 = xk - alpha * gradienteX
            if (distancia_origen(x_k1-xk)/distancia_origen(xk)+0.00001) <= epsilon2:
                terminar = True
            else:
                k = k + 1
                xk = x_k1
    return xk




