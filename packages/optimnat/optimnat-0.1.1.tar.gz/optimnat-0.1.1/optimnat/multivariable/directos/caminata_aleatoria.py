import numpy as np
from typing import Callable, Tuple, List

def random_walk(f: Callable[[float], float],
                terminar: Callable[[float], bool],
                x0: float,
                generacion_aleatoria: Callable[[float], float]) -> Tuple[float, List[float]]:
    """
    Realiza una búsqueda aleatoria para encontrar el mínimo de una función unidimensional.

    Parámetros:
    ----------
    f : Callable[[float], float]
        La función objetivo que se desea minimizar.
    terminar : Callable[[float], bool]
        La función de criterio de terminación que indica cuándo detener la búsqueda.
    x0 : float
        El punto inicial de la búsqueda.
    generacion_aleatoria : Callable[[float], float]
        Función que genera pasos aleatorios basados en el punto actual.

    Retorna:
    -------
    x_mejor : float
        El punto que minimiza la función.
    historial_puntos : List[float]
        El historial de todos los puntos visitados durante la búsqueda.
    """
    x_mejor = x0
    x_actual = x0
    historial_puntos = [x_actual]  # Para almacenar todos los puntos visitados

    while not terminar(x_actual):
        x_siguiente = generacion_aleatoria(x_actual)
        if f(x_siguiente) < f(x_mejor):
            x_mejor = x_siguiente
        x_actual = x_siguiente
        historial_puntos.append(x_actual)  # Guardar el punto visitado en el historial
    
    return x_mejor, historial_puntos

# Criterio de terminación
def _criterio_terminacion(x: float, max_iter: int = 100) -> bool:
    """
    Criterio de terminación para la búsqueda aleatoria.

    Parámetros:
    ----------
    x : float
        El punto actual en la búsqueda.
    max_iter : int, opcional
        Número máximo de iteraciones permitidas antes de terminar la búsqueda (default=100).

    Retorna:
    -------
    bool
        True si se debe terminar la búsqueda, False de lo contrario.
    """
    _criterio_terminacion.iteraciones += 1
    return _criterio_terminacion.iteraciones >= max_iter

# Inicialización del contador de iteraciones
_criterio_terminacion.iteraciones = 0

# Generación de pasos aleatorios
def _generacion_aleatoria(x: float, mu: float = 0, sigma: float = 0.5) -> float:
    """
    Genera un paso aleatorio basado en el punto actual x.

    Parámetros:
    ----------
    x : float
        El punto actual en la búsqueda.
    mu : float, opcional
        Media de la distribución normal para la generación aleatoria (default=0).
    sigma : float, opcional
        Desviación estándar de la distribución normal para la generación aleatoria (default=0.5).

    Retorna:
    -------
    float
        El próximo punto generado aleatoriamente.
    """
    return x + np.random.normal(mu, sigma)
