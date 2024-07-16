import numpy as np    
from typing import Callable, Tuple, List, Dict, Any

def hooke_jeeves(
    f: Callable[[np.ndarray], float],
    x0: np.ndarray,
    delta: np.ndarray,
    alpha: float,
    epsilon: float,
    max_iter: int
) -> Tuple[np.ndarray, List[np.ndarray]]:
    """
    Implementación del método de optimización Hooke-Jeeves.

    Parámetros:
    ----------
    f : Callable[[np.ndarray], float]
        Función objetivo que se desea minimizar.
    x0 : np.ndarray
        Punto inicial de búsqueda.
    delta : np.ndarray
        Vector de pasos inicial.
    alpha : float
        Factor de reducción de delta.
    epsilon : float
        Criterio de convergencia para la norma de delta.
    max_iter : int
        Número máximo de iteraciones permitidas.

    Retorna:
    -------
    xk : np.ndarray
        Punto óptimo encontrado.
    history : List[np.ndarray]
        Historial de puntos visitados durante la optimización.
    """

    def _exploratory_move(xc: np.ndarray, delta: np.ndarray) -> np.ndarray:
        """
        Realiza un movimiento exploratorio alrededor del punto actual.

        Parámetros:
        ----------
        xc : np.ndarray
            Punto actual.
        delta : np.ndarray
            Vector de pasos.

        Retorna:
        -------
        x : np.ndarray
            Nuevo punto después del movimiento exploratorio.
        """
        x = np.copy(xc)
        for i in range(len(x)):
            f_plus = f(x + delta * np.eye(1, len(x), i).flatten())
            f_minus = f(x - delta * np.eye(1, len(x), i).flatten())
            if f_plus < f(x):
                x[i] += delta[i]
            elif f_minus < f(x):
                x[i] -= delta[i]
        return x

    xk = np.copy(x0)
    k = 0
    history = [np.copy(xk)]
    
    while np.linalg.norm(delta) > epsilon and k < max_iter:
        # Paso 2: Realiza un movimiento exploratorio
        xc = np.copy(xk)
        x = _exploratory_move(xc, delta)
        
        if np.array_equal(x, xc):
            # Paso 3: Reduce delta si no hubo mejoría
            delta /= alpha
        else:
            # Paso 4: Realiza un movimiento patrón
            xk = x
            xp = xk + (xk - xc)
            # Paso 5: Realiza otro movimiento exploratorio con xp
            xk1 = _exploratory_move(xp, delta)
            # Paso 6: Compara f(xk1) con f(xk)
            if f(xk1) < f(xk):
                xk = xk1
            k += 1
        history.append(np.copy(xk))
        
    return xk, history