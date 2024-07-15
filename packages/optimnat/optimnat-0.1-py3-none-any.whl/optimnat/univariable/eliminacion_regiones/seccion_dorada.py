import numpy as np
from typing import Callable, List, Tuple

def golden_section_search(
    a: float,
    b: float,
    epsilon: float,
    func: Callable[[float], float]
) -> Tuple[float, float, List[Tuple[float, float, float, float, float, float]]]:
    """
    Implementa el método de búsqueda de la sección dorada para la optimización de funciones unidimensionales.

    Parámetros:
    ----------
    a : float
        Límite inferior del intervalo inicial de búsqueda.
    b : float
        Límite superior del intervalo inicial de búsqueda.
    epsilon : float
        Criterio de convergencia. El algoritmo termina cuando el tamaño del intervalo es menor que epsilon.
    func : Callable[[float], float]
        Función objetivo que se desea minimizar.

    Retorna:
    -------
    x_opt : float
        El punto que minimiza la función en el intervalo [a, b].
    f_opt : float
        El valor de la función en el punto óptimo.
    history : List[Tuple[float, float, float, float, float, float]]
        Historial de intervalos y puntos evaluados durante la optimización.
        Cada entrada es una tupla (a, b, x1, fx1, x2, fx2).
    """
    # Definición de la constante dorada
    phi = (1 + np.sqrt(5)) / 2
    resphi = 2 - phi

    # Inicialización
    Lw = 1
    history = []

    # Normalización de las variables
    x1 = a + resphi * (b - a)
    x2 = b - resphi * (b - a)
    fx1 = func(x1)
    fx2 = func(x2)

    # Iteraciones del algoritmo
    while (b - a) > epsilon:
        if fx1 < fx2:
            b = x2
            x2 = x1
            fx2 = fx1
            x1 = a + resphi * (b - a)
            fx1 = func(x1)
        else:
            a = x1
            x1 = x2
            fx1 = fx2
            x2 = b - resphi * (b - a)
            fx2 = func(x2)

        Lw = b - a
        history.append((a, b, x1, fx1, x2, fx2))

    if fx1 < fx2:
        return x1, fx1, history
    else:
        return x2, fx2, history