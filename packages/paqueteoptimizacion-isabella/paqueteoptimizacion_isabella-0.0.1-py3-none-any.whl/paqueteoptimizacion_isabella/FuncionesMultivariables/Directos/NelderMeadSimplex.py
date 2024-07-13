import numpy as np

def nelder_mead(f, x_start, gamma, beta, alpha, tol=1e-5, max_iter=1000):
    """
    Implementa el método Nelder-Mead para la optimización de funciones sin derivadas.
    Este método es efectivo para optimización de funciones no lineales sin necesidad 
    de derivadas, utilizando operaciones simples como reflexiones, expansiones y 
    contracciones en un simplex que se adapta dinámicamente durante las iteraciones.

    :Example:

    >>> def f(x):
    ...     return sum(xi**2 for xi in x)
    >>> x_start = np.array([1.0, 1.0])
    >>> gamma = 2.0
    >>> beta = 0.5
    >>> alpha = 1.0
    >>> nelder_mead(f, x_start, gamma, beta, alpha)
    array([0., 0.])

    :param f: La función objetivo a minimizar.
    :type f: callable
    :param x_start: El punto inicial de la búsqueda.
    :type x_start: ndarray
    :param gamma: Parámetro gamma para la reflexión.
    :type gamma: float
    :param beta: Parámetro beta para la contracción.
    :type beta: float
    :param alpha: Parámetro alpha para la expansión.
    :type alpha: float
    :param tol: Tolerancia de convergencia. Default es 1e-5.
    :type tol: float, optional
    :param max_iter: Número máximo de iteraciones. Default es 1000.
    :type max_iter: int, optional
    :return: El punto óptimo encontrado.
    :rtype: ndarray
    """

    N = len(x_start)

    def create_initial_simplex(x0, alpha=1.0):
        simplex = np.zeros((N + 1, N))
        simplex[0] = x0
        for i in range(1, N + 1):
            x = x0.copy()
            x[i - 1] += alpha
            simplex[i] = x
        return simplex

    def sort_simplex(simplex, f):
        indices = np.argsort([f(x) for x in simplex])
        return simplex[indices]

    simplex = create_initial_simplex(x_start)
    
    for iteration in range(max_iter):
        simplex = sort_simplex(simplex, f)
        xc = np.mean(simplex[:-1], axis=0)
        xr = 2 * xc - simplex[-1]

        if f(xr) < f(simplex[0]):
            xe = xc + gamma * (xc - simplex[-1])
            if f(xe) < f(xr):
                simplex[-1] = xe
            else:
                simplex[-1] = xr
        else:
            if f(xr) < f(simplex[-2]):
                simplex[-1] = xr
            else:
                if f(xr) < f(simplex[-1]):
                    xc_out = xc + beta * (xr - xc)
                    if f(xc_out) < f(xr):
                        simplex[-1] = xc_out
                    else:
                        for i in range(1, N + 1):
                            simplex[i] = simplex[0] + 0.5 * (simplex[i] - simplex[0])
                else:
                    xc_in = xc - beta * (xc - simplex[-1])
                    if f(xc_in) < f(simplex[-1]):
                        simplex[-1] = xc_in
                    else:
                        for i in range(1, N + 1):
                            simplex[i] = simplex[0] + 0.5 * (simplex[i] - simplex[0])

        if np.sqrt(np.mean([(f(x) - f(simplex[0]))**2 for x in simplex])) <= tol:
            break

    simplex = sort_simplex(simplex, f)
    return simplex[0]
