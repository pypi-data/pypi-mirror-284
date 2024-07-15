from typing import Callable, List, Tuple

def _derivada(f: Callable[[float], float], x: float, delta: float) -> float:
    """
    Calcula la derivada de una función en un punto dado utilizando una aproximación de diferencias finitas hacia adelante.

    Parámetros:
    ----------
    f : Callable[[float], float]
        La función objetivo cuya derivada se desea calcular.
    x : float
        El punto en el cual se evalúa la derivada.
    delta : float
        El pequeño incremento utilizado para calcular la derivada.

    Retorna:
    -------
    float
        La derivada de la función en el punto x.
    """
    return (f(x + delta) - f(x)) / delta

def _segunda_derivada(f: Callable[[float], float], x: float, delta: float) -> float:
    """
    Calcula la segunda derivada de una función en un punto dado utilizando una aproximación de diferencias finitas centradas.

    Parámetros:
    ----------
    f : Callable[[float], float]
        La función objetivo cuya segunda derivada se desea calcular.
    x : float
        El punto en el cual se evalúa la segunda derivada.
    delta : float
        El pequeño incremento utilizado para calcular la segunda derivada.

    Retorna:
    -------
    float
        La segunda derivada de la función en el punto x.
    """
    return (f(x + delta) - 2 * f(x) + f(x - delta)) / (delta ** 2)

def _delta_x(x: float) -> float:
    """
    Calcula un pequeño incremento basado en el valor absoluto de x para utilizar en las derivadas.

    Parámetros:
    ----------
    x : float
        El punto en el cual se calcula el incremento.

    Retorna:
    -------
    float
        El pequeño incremento calculado.
    """
    return 1e-5 * (abs(x) + 1e-5)

def newton_method(x0: float, epsilon: float, f: Callable[[float], float]) -> Tuple[float, List[Tuple[float, float, float, float]]]:
    """
    Implementa el método de Newton para encontrar el mínimo de una función unidimensional.

    Parámetros:
    ----------
    x0 : float
        El punto inicial para el algoritmo de Newton.
    epsilon : float
        El criterio de convergencia. El algoritmo termina cuando la magnitud de la derivada es menor que epsilon.
    f : Callable[[float], float]
        La función objetivo que se desea minimizar.

    Retorna:
    -------
    x_opt : float
        El punto que minimiza la función.
    history : List[Tuple[float, float, float, float]]
        El historial de puntos evaluados durante la optimización.
        Cada entrada es una tupla (x, f(x), f'(x), f''(x)).
    """
    x = x0
    history = []

    while True:
        fx_prime = _derivada(f, x, _delta_x(x))
        fx_double_prime = _segunda_derivada(f, x, _delta_x(x))
        
        if abs(fx_prime) < epsilon:
            break
        
        if fx_double_prime == 0:
            break
        
        x_next = x - fx_prime / fx_double_prime
        history.append((x, f(x), fx_prime, fx_double_prime))
        
        x = x_next

    history.append((x, f(x), fx_prime, fx_double_prime))
    return x, history