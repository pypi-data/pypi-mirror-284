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




# ------------------------------------ GRADIENTE CONJUGADO ------------------------------------ 
def gradiente_conjugado(f_o, x0, metodo_busqueda, e1=1e-6, e2=1e-6, e3=1e-6):
    """
    Implementa el método del Gradiente Conjugado para la optimización de funciones.
    El método del gradiente conjugado utiliza tanto la información del gradiente en 
    la iteración actual como la de iteraciones previas para calcular la dirección de 
    búsqueda siguiente.

    :Example:

    >>> def f_o(x):
    ...     return sum(xi**2 for xi in x)
    >>> def metodo_busqueda(alpha_funcion, e1, a, b):
    ...     return 0.1  # Dummy implementation for example
    >>> x0 = np.array([1.0, 1.0])
    >>> gradiente_conjugado(f_o, x0, metodo_busqueda)
    array([0., 0.])

    :param f_o: La función objetivo a minimizar.
    :type f_o: callable
    :param x0: Punto inicial de búsqueda.
    :type x0: ndarray
    :param metodo_busqueda: Método de búsqueda para calcular el paso alpha.
    :type metodo_busqueda: callable
    :param e1: Tolerancia para la búsqueda de línea. Default es 1e-6.
    :type e1: float, optional
    :param e2: Tolerancia para la condición de convergencia basada en la diferencia relativa. Default es 1e-6.
    :type e2: float, optional
    :param e3: Tolerancia para la condición de convergencia basada en la norma del gradiente. Default es 1e-6.
    :type e3: float, optional
    :return: Punto óptimo encontrado.
    :rtype: ndarray
    """

    x = x0
    grad = gradiente(f_o, x)
    s = -grad
    k = 0

    def line_search(f_o, x, s, e1):
        def alpha_funcion(alpha):
            return f_o(x + alpha * s)
        return metodo_busqueda(alpha_funcion, e1, 0.0, 1.0)

    while True:
        alpha = line_search(f_o, x, s, e1)
        x_next = x + alpha * s
        grad_next = gradiente(f_o, x_next)

        if np.linalg.norm(x_next - x) / (np.linalg.norm(x) + 1e-8) <= e2 or np.linalg.norm(grad_next) <= e3:
            break

        beta = np.dot(grad_next, grad_next) / np.dot(grad, grad)
        s = -grad_next + beta * s

        x = x_next
        grad = grad_next
        k += 1

    return x




