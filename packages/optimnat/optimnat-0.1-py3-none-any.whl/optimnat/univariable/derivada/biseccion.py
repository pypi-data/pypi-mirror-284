from typing import Callable, List, Tuple

def _derivada(f: Callable[[float], float], x: float, deltaa_x: float) -> float:
    """
    Calcula la derivada de una función en un punto dado utilizando una aproximación de diferencias finitas centradas.

    Parámetros:
    ----------
    f : Callable[[float], float]
        La función objetivo cuya derivada se desea calcular.
    x : float
        El punto en el cual se evalúa la derivada.
    deltaa_x : float
        El pequeño incremento utilizado para calcular la derivada.

    Retorna:
    -------
    float
        La derivada de la función en el punto x.
    """
    return (f(x + deltaa_x) - f(x - deltaa_x)) / (2 * deltaa_x)

def _segunda_derivada(f: Callable[[float], float], x: float, deltaa_x: float) -> float:
    """
    Calcula la segunda derivada de una función en un punto dado utilizando una aproximación de diferencias finitas centradas.

    Parámetros:
    ----------
    f : Callable[[float], float]
        La función objetivo cuya segunda derivada se desea calcular.
    x : float
        El punto en el cual se evalúa la segunda derivada.
    deltaa_x : float
        El pequeño incremento utilizado para calcular la segunda derivada.

    Retorna:
    -------
    float
        La segunda derivada de la función en el punto x.
    """
    return (f(x + deltaa_x) - 2 * f(x) + f(x - deltaa_x)) / (deltaa_x ** 2)

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
    if abs(x) > 0.01:
        return 0.01 * abs(x)
    else:
        return 0.0001

def biseccion(a: float, b: float, epsilon: float, f: Callable[[float], float]) -> Tuple[float, List[Tuple[float, float, float, float, float]]]:
    """
    Implementa el método de bisección para encontrar el mínimo de una función unidimensional.

    Parámetros:
    ----------
    a : float
        El límite inferior del intervalo de búsqueda.
    b : float
        El límite superior del intervalo de búsqueda.
    epsilon : float
        El criterio de convergencia. El algoritmo termina cuando la magnitud de la derivada es menor que epsilon.
    f : Callable[[float], float]
        La función objetivo que se desea minimizar.

    Retorna:
    -------
    z_opt : float
        El punto que minimiza la función.
    history : List[Tuple[float, float, float, float, float]]
        El historial de puntos evaluados durante la optimización.
        Cada entrada es una tupla (x1, x2, z, f(z), f'(z)).
    """
    x1, x2 = a, b
    z = (x1 + x2) / 2
    history = []

    while abs(_derivada(f, z, _delta_x(z))) > epsilon:
        z = (x1 + x2) / 2
        history.append((x1, x2, z, f(z), _derivada(f, z, _delta_x(z))))

        if _derivada(f, z, _delta_x(z)) < 0:
            x1 = z
        else:
            x2 = z

    history.append((x1, x2, z, f(z), _derivada(f, z, _delta_x(z))))
    return z, history
