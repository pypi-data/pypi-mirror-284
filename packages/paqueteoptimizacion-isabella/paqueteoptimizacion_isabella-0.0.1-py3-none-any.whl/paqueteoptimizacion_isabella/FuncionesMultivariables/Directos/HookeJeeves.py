import numpy as np

def exploratory_move(x, deltas, objective_function):
    """
    Realiza un movimiento exploratorio en el espacio de búsqueda.

    :Example:

    >>> def objective_function(x):
    ...     return sum(xi**2 for xi in x)
    >>> x = [0, 0]
    >>> deltas = [1, 1]
    >>> exploratory_move(x, deltas, objective_function)
    [1, 0]

    :param x: El punto actual.
    :type x: list
    :param deltas: Los tamaños de paso para cada dimensión.
    :type deltas: list
    :param objective_function: La función objetivo a minimizar.
    :type objective_function: callable
    :return: El mejor punto encontrado durante la exploración.
    :rtype: list
    """
    n = len(x)
    best_x = x[:]
    best_value = objective_function(x)
    for i in range(n):
        x_new = x[:]
        x_new[i] += deltas[i]
        new_value = objective_function(x_new)
        if new_value < best_value:
            best_x = x_new[:]
            best_value = new_value
        x_new = x[:]
        x_new[i] -= 2 * deltas[i]
        new_value = objective_function(x_new)
        if new_value < best_value:
            best_x = x_new[:]
            best_value = new_value
    return best_x




def pattern_move(xk, xk_1):
    """
    Realiza un movimiento de patrón en el espacio de búsqueda.

    :Example:

    >>> xk = [1, 2]
    >>> xk_1 = [0, 1]
    >>> pattern_move(xk, xk_1)
    [2, 3]

    :param xk: El punto actual.
    :type xk: list
    :param xk_1: El punto anterior.
    :type xk_1: list
    :return: El nuevo punto obtenido mediante el movimiento de patrón.
    :rtype: list
    """
    return [xk[i] + (xk[i] - xk_1[i]) for i in range(len(xk))]







def hooke_jeeves(x0, deltas, alpha, epsilon, objective_function):
    """
    Realiza la optimización usando el método de Hooke y Jeeves. El método de 
    Hooke-Jeeves es un algoritmo de optimización directa utilizado para encontrar 
    el mínimo de una función objetivo sin necesidad de derivadas.

    :Example:

    >>> def objective_function(x):
    ...     return sum(xi**2 for xi in x)
    >>> x0 = [0, 0]
    >>> deltas = [1, 1]
    >>> alpha = 2
    >>> epsilon = 0.01
    >>> hooke_jeeves(x0, deltas, alpha, epsilon, objective_function)
    [0, 0]

    :param x0: El punto inicial de la búsqueda.
    :type x0: list
    :param deltas: Los tamaños de paso iniciales para cada dimensión.
    :type deltas: list
    :param alpha: El factor de reducción para los tamaños de paso.
    :type alpha: float
    :param epsilon: La tolerancia para la convergencia.
    :type epsilon: float
    :param objective_function: La función objetivo a minimizar.
    :type objective_function: callable
    :return: El punto óptimo encontrado.
    :rtype: list
    """

    xk = x0[:]
    xk_1 = x0[:]
    k = 0

    while np.linalg.norm(deltas) > epsilon:
        xk_new = exploratory_move(xk, deltas, objective_function)
        
        if xk_new != xk:
            xk_1 = xk[:]
            xk = xk_new[:]
            xk_p = pattern_move(xk, xk_1)
            xk_new = exploratory_move(xk_p, deltas, objective_function)
            
            if objective_function(xk_new) < objective_function(xk):
                xk = xk_new[:]
        else:
            if max(deltas) < epsilon:
                break
            deltas = [delta / alpha for delta in deltas]
    
    return xk

