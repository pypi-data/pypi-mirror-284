import numpy as np
from typing import Callable, Tuple, List, Dict, Any

def gradiente_conjugado(
    f: Callable[[np.ndarray], float],
    grad_f: Callable[[np.ndarray], np.ndarray],
    x0: np.ndarray,
    epsilon1: float = 1e-6,
    epsilon2: float = 1e-6,
    epsilon3: float = 1e-6
) -> Dict[str, Any]:
    """
    Implementación del método de gradiente conjugado para la optimización de funciones.

    Parámetros:
    ----------
    f : Callable[[np.ndarray], float]
        Función objetivo que se desea minimizar.
    grad_f : Callable[[np.ndarray], np.ndarray]
        Función que calcula el gradiente de la función objetivo.
    x0 : np.ndarray
        Punto inicial de búsqueda.
    epsilon1 : float, opcional
        Criterio de convergencia para la búsqueda de línea (por defecto 1e-6).
    epsilon2 : float, opcional
        Criterio de convergencia para la diferencia en x (por defecto 1e-6).
    epsilon3 : float, opcional
        Criterio de convergencia para la norma del gradiente (por defecto 1e-6).

    Retorna:
    -------
    dict
        Diccionario con el punto óptimo, valor óptimo, número de iteraciones y trayectoria de la optimización.
    """
    x = x0
    grad = grad_f(x)
    s = -grad
    k = 0
    trayectoria = [(x, f(x))]  # Para almacenar la trayectoria de la optimización
    
    while True:
        # Paso 3: Encontrar λ^(0) tal que f(x^(0) + λ^(0)s^(0)) sea mínimo con terminación epsilon1
        lambda_ = _busqueda_linea(lambda l: f(x + l * s), 0, 1, epsilon1)
        x_nuevo = x + lambda_ * s
        grad_nuevo = grad_f(x_nuevo)
        
        # Paso 6: Condiciones de terminación
        if np.linalg.norm(x_nuevo - x) <= epsilon2 or np.linalg.norm(grad_nuevo) <= epsilon3:
            break
        
        # Paso 4: Actualizar s
        if np.linalg.norm(grad) != 0:
            beta = np.dot(grad_nuevo, grad_nuevo) / np.dot(grad, grad)
        else:
            beta = 0  # Evitar división por cero
        
        s = -grad_nuevo + beta * s
        
        # Actualizar x y grad
        x = x_nuevo
        grad = grad_nuevo
        trayectoria.append((x, f(x)))
        k += 1
        
    return {
        'punto_optimo': x,
        'valor_optimo': f(x),
        'iteraciones': k,
        'trayectoria': trayectoria
    }

def _busqueda_linea(
    phi: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-5
) -> float:
    """
    Implementación de búsqueda de línea usando el método de la sección dorada.

    Parámetros:
    ----------
    phi : Callable[[float], float]
        Función unidimensional a minimizar.
    a : float
        Límite inferior del intervalo de búsqueda.
    b : float
        Límite superior del intervalo de búsqueda.
    tol : float, opcional
        Tolerancia para la convergencia (por defecto 1e-5).

    Retorna:
    -------
    float
        El valor de λ que minimiza phi en el intervalo [a, b].
    """
    invphi = (np.sqrt(5) - 1) / 2  # 1 / phi
    invphi2 = (3 - np.sqrt(5)) / 2  # 1 / phi^2
    
    c = b - invphi * (b - a)
    d = a + invphi * (b - a)
    phi_c, phi_d = phi(c), phi(d)
    
    while abs(c - d) > tol:
        if phi_c < phi_d:
            b, phi_b = d, phi_d
            d, phi_d = c, phi_c
            c = b - invphi * (b - a)
            phi_c = phi(c)
        else:
            a, phi_a = c, phi_c
            c, phi_c = d, phi_d
            d = a + invphi * (b - a)
            phi_d = phi(d)
    
    if phi_c < phi_d:
        return c
    else:
        return d
