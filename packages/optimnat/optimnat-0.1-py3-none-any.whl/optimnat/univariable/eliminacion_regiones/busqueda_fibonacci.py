from typing import Callable, List, Tuple

def _fibonacci_numbers(n: int) -> List[int]:
    """
    Genera una lista de números de Fibonacci hasta el n-ésimo número de Fibonacci.

    Parámetros:
    ----------
    n : int
        La cantidad de números de Fibonacci a generar.

    Retorna:
    -------
    List[int]
        Lista de números de Fibonacci.
    """
    fibs = [1, 1]
    for i in range(2, n + 2):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs

def fibonacci_search_method(
    a: float,
    b: float,
    n: int,
    funcion: Callable[[float], float]
) -> Tuple[float, float, List[Tuple[float, float, float, float, float, float]]]:
    """
    Implementa el método de búsqueda de Fibonacci para la optimización de funciones unidimensionales.

    Parámetros:
    ----------
    a : float
        Límite inferior del intervalo inicial de búsqueda.
    b : float
        Límite superior del intervalo inicial de búsqueda.
    n : int
        Número de iteraciones basado en los números de Fibonacci.
    funcion : Callable[[float], float]
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
    fibs = _fibonacci_numbers(n)
    L = b - a
    k = 1
    history = []

    x1 = a + (fibs[n - k] / fibs[n + 1]) * L
    x2 = b - (fibs[n - k] / fibs[n + 1]) * L
    fx1 = funcion(x1)
    fx2 = funcion(x2)
    
    while k <= n:
        if fx1 < fx2:
            b = x2
            x2 = x1
            x1 = a + (fibs[n - k] / fibs[n + 1]) * (b - a)
            fx2 = fx1
            fx1 = funcion(x1)
        else:
            a = x1
            x1 = x2
            x2 = b - (fibs[n - k] / fibs[n + 1]) * (b - a)
            fx1 = fx2
            fx2 = funcion(x2)

        history.append((a, b, x1, fx1, x2, fx2))
        k += 1

    if fx1 < fx2:
        return x1, fx1, history
    else:
        return x2, fx2, history
