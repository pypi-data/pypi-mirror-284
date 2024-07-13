import random
import numpy as np


def caminata_aleatoria(func, x0, paso, iteraciones=1000):
    """
    Realiza una búsqueda de optimización usando el método de Caminata Aleatoria.
    La caminata aleatoria es un proceso donde el punto se mueve paso a paso en direcciones 
    aleatorias dentro de un espacio, un plano o un espacio de mayor dimensión. Cada paso en 
    este proceso es independiente de los anteriores.

    :Example:

    >>> import numpy as np
    >>> def func(x):
    ...     return np.sum(x**2)
    >>> x0 = np.array([1.0, 1.0])
    >>> paso = 0.1
    >>> caminata_aleatoria(func, x0, paso)
    array([0.0002154, 0.0005237])

    :param func: La función objetivo a minimizar.
    :type func: callable
    :param x0: El punto inicial de la búsqueda.
    :type x0: ndarray
    :param iteraciones: El número de iteraciones de la búsqueda. Default es 1000.
    :type iteraciones: int, optional
    :param paso: El tamaño del paso en cada iteración. Recomendacion de 0.1.
    :type paso: float
    :return: El punto óptimo encontrado.
    :rtype: ndarray
    :raises: TypeError
    """
    x = x0
    for i in range(iteraciones):
        x_nuevo = x + np.random.uniform(-paso, paso, size=x.shape)
        if func(x_nuevo) < func(x):
            x = x_nuevo
    return x


