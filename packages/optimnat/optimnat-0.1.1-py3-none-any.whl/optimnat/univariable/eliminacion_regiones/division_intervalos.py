from typing import Callable, List, Tuple

def intervalos_por_mitad(
    a: float,
    b: float,
    epsilon: float,
    funcion: Callable[[float], float]
) -> Tuple[float, List[Tuple[float, float]]]:
    """
    Implementa el método de intervalos por mitad (bisección) para la optimización de funciones unidimensionales.

    Parámetros:
    ----------
    a : float
        Límite inferior del intervalo inicial de búsqueda.
    b : float
        Límite superior del intervalo inicial de búsqueda.
    epsilon : float
        Criterio de convergencia. El algoritmo termina cuando el tamaño del intervalo es menor que epsilon.
    funcion : Callable[[float], float]
        Función objetivo que se desea minimizar.

    Retorna:
    -------
    xm : float
        El punto que minimiza la función en el intervalo [a, b].
    history : List[Tuple[float, float]]
        Historial de puntos medios y sus valores de función durante la optimización.
    """
    
    L0 = b - a
    xm = (a + b) / 2.0
    fxm = funcion(xm)
    history = [(xm, fxm)]

    while True:
        L = b - a
        x1 = a + L / 4.0
        x2 = b - L / 4.0
        fx1 = funcion(x1)
        fx2 = funcion(x2)

        if fx1 < fxm:
            b = xm
            xm = x1
            fxm = fx1
        elif fx2 < fxm:
            a = xm
            xm = x2
            fxm = fx2
        else:
            a = x1
            b = x2

        L = b - a
        history.append((xm, fxm))
        
        if abs(L) < epsilon:
            break
    
    return xm, history
