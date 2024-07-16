import numpy as np
from typing import Callable, Tuple, List

def nelder_mead(f: Callable[[np.ndarray], float],
                x0: np.ndarray,
                gamma: float = 2,
                beta: float = 0.5,
                epsilon: float = 1e-5,
                max_iter: int = 1000) -> Tuple[np.ndarray, List[List[float]]]:
    """
    Implementa el método Nelder-Mead para encontrar el mínimo de una función multidimensional.

    Parámetros:
    ----------
    f : Callable[[np.ndarray], float]
        La función objetivo que se desea minimizar.
    x0 : np.ndarray
        El punto inicial de la búsqueda.
    gamma : float, opcional
        Parámetro de expansión para la fase de expansión (default=2).
    beta : float, opcional
        Parámetro de contracción para la fase de contracción (default=0.5).
    epsilon : float, opcional
        Criterio de convergencia. El algoritmo termina cuando la desviación estándar de
        los valores de la función es menor o igual a epsilon (default=1e-5).
    max_iter : int, opcional
        Número máximo de iteraciones permitidas (default=1000).

    Retorna:
    -------
    x_optimo : np.ndarray
        El punto que minimiza la función.
    historial_puntos : List[List[float]]
        El historial de puntos evaluados durante la optimización.
        Cada entrada es una lista que representa un punto en el espacio de búsqueda.
    """
    N = len(x0)
    # Crear el simplex inicial
    simplex = [x0]
    for i in range(N):
        x = np.copy(x0)
        x[i] = x[i] + (x[i] + 1)
        simplex.append(x)
    simplex = np.array(simplex)

    historial_puntos = [simplex[0].tolist()]  # Inicializar con el mejor punto

    for iteration in range(max_iter):
        # Ordenar el simplex según los valores de la función objetivo
        simplex = sorted(simplex, key=lambda x: f(x))
        xh = simplex[-1]   # El peor punto
        xl = simplex[0]    # El mejor punto
        xg = simplex[-2]   # El siguiente peor punto

        # Calcular el centroide
        xc = np.mean(simplex[:-1], axis=0)

        # Reflejar el punto xh
        xr = 2 * xc - xh
        if f(xr) < f(xl):
            # Expansión
            xe = (1 + gamma) * xc - gamma * xh
            if f(xe) < f(xr):
                xnew = xe
            else:
                xnew = xr
        elif f(xr) < f(xg):
            xnew = xr
        else:
            if f(xr) < f(xh):
                xh = xr
            # Contracción
            if f(xr) < f(xh):
                xc = xc - beta * (xc - xr)
            else:
                xc = xc - beta * (xc - xh)
            xnew = xc

        # Reemplazar el peor punto con el nuevo punto
        simplex[-1] = xnew

        # Guardar el historial de puntos visitados
        historial_puntos.append(xl.tolist())

        # Comprobar la condición de terminación
        f_values = np.array([f(x) for x in simplex])
        if np.sqrt(np.sum((f_values - np.mean(f_values)) ** 2) / (N + 1)) <= epsilon:
            break

    return xl, historial_puntos
