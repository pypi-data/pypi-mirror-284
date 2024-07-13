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

# ---------------------------------- HESSIANA ---------------------------------- 
def hessiana(funcion, x, delta=0.001):
    """
    Calcula la matriz Hessiana de una función en un punto dado.
    
    :Example:
    
    >>> def funcion(x):
    ...     return x[0]**2 + x[1]**2
    >>> x = np.array([1.0, 2.0])
    >>> hessiana(funcion, x)
    array([[2., 0.],
           [0., 2.]])

    :param funcion: La función para la cual se calcula la Hessiana.
    :type funcion: callable
    :param x: El punto en el que se calcula la Hessiana.
    :type x: ndarray
    :param delta: El tamaño del paso para el cálculo de diferencias finitas. Default es 0.001.
    :type delta: float, optional
    :return: La matriz Hessiana calculada.
    :rtype: ndarray
    """
    n = len(x)
    matriz = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                copia1 = x.copy()
                copia1[i] += delta
                f1 = funcion(copia1)
                
                copia2 = x.copy()
                copia2[i] -= delta
                f2 = funcion(copia2)
                
                matriz[i, i] = (f1 - 2 * funcion(x) + f2) / (delta**2)
            elif i < j:
                copia3 = x.copy()
                copia3[i] += delta
                copia3[j] += delta
                f3 = funcion(copia3)
                
                copia4 = x.copy()
                copia4[i] += delta
                copia4[j] -= delta
                f4 = funcion(copia4)
                
                copia5 = x.copy()
                copia5[i] -= delta
                copia5[j] += delta
                f5 = funcion(copia5)
                
                copia6 = x.copy()
                copia6[i] -= delta
                copia6[j] -= delta
                f6 = funcion(copia6)
                
                matriz[i, j] = (f3 - f4 - f5 + f6) / (4 * delta * delta)
                matriz[j, i] = matriz[i, j]
    return matriz


# ---------------------------------- DISTANCIA ORIGEN ---------------------------------- 
def distancia_origen(vector):
    """
    Calcula la distancia de un vector al origen.
    
    :Example:
    
    >>> vector = np.array([3, 4])
    >>> distancia_origen(vector)
    5.0

    :param vector: El vector del cual se calculará la distancia.
    :type vector: ndarray
    :return: La distancia del vector al origen.
    :rtype: float
    """
    return np.linalg.norm(vector)

# ---------------------------------- MÉTODO DE NEWTON MODIFICADO ---------------------------------- 
def newton(funcion_objetivo, x0, metodo_busqueda, epsilon1=1e-6, epsilon2=1e-6, max_iterations=100):
    """
    Implementa el método de Newton modificado para la optimización de funciones.
    El Método de Newton es un algoritmo de optimización que busca encontrar 
    raíces de funciones o mínimos de funciones derivadas.

    :Example:

    >>> def funcion_objetivo(x):
    ...     return x[0]**2 + x[1]**2
    >>> def metodo_busqueda(alpha_funcion, epsilon2, a, b):
    ...     return 0.1  # Implementación dummy para el ejemplo
    >>> x0 = [1.0, 1.0]
    >>> newton(funcion_objetivo, x0, metodo_busqueda)
    array([0., 0.])

    :param funcion_objetivo: Función objetivo a minimizar.
    :type funcion_objetivo: callable
    :param x0: Punto inicial de búsqueda.
    :type x0: list
    :param metodo_busqueda: Método de búsqueda para calcular el paso alpha.
    :type metodo_busqueda: callable
    :param epsilon1: Tolerancia para la norma del gradiente. Default es 1e-6.
    :type epsilon1: float, optional
    :param epsilon2: Tolerancia para la diferencia relativa entre iteraciones sucesivas. Default es 1e-6.
    :type epsilon2: float, optional
    :param max_iterations: Número máximo de iteraciones permitidas. Default es 100.
    :type max_iterations: int, optional
    :return: Punto óptimo encontrado.
    :rtype: ndarray
    """

    terminar = False
    xk = np.array(x0, dtype=float)
    k = 0
    while not terminar:
        # GRADIENTE
        gradienteX = gradiente(funcion_objetivo, xk)
        
        if np.linalg.norm(gradienteX) < epsilon1 or k >= max_iterations:
            terminar = True
        else:
            # HESSIANA
            hessian = hessiana(funcion_objetivo, xk)
            try:
                inversa = np.linalg.inv(hessian)
            except np.linalg.LinAlgError:
                print("La matriz Hessiana no es invertible.")
                return None
            
            # PRODUCTO PUNTO
            punto = np.dot(inversa, gradienteX)
            

            def alpha_calcular(alpha):
                return funcion_objetivo(xk - alpha * punto)
            
            alpha = metodo_busqueda(alpha_calcular, epsilon2, 0.0, 1.0)
            
            x_k1 = xk - alpha * punto

            if (distancia_origen(x_k1 - xk) / (distancia_origen(xk) + 0.00001)) <= epsilon2:
                terminar = True
            else:
                k += 1
                xk = x_k1
        

    if k < max_iterations:
        print(f"Convergencia alcanzada en {k+1} iteraciones")
    else:
        print("El método no convergió")
    
    return xk





