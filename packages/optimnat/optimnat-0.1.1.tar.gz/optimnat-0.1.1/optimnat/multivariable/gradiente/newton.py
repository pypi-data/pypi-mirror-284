import numpy as np
import math

def _regla_eliminacion(x1, x2, fx1, fx2, a, b):
    """
    Aplica la regla de eliminación para determinar los límites actualizados según los valores de la función.

    Args:
    - x1, x2: Los puntos candidatos para la regla de eliminación.
    - fx1, fx2: Los valores de la función en x1 y x2, respectivamente.
    - a, b: Los límites originales del intervalo.

    Returns:
    - Tuple[float, float]: Los límites actualizados después de aplicar la regla de eliminación.
    """
    if fx1 > fx2:
        return x1, b

    if fx1 < fx2:
        return a, x2
    
    return x1, x2

def _w_to_x(w, a, b):
    """
    Convierte un valor w en el intervalo [0, 1] a un valor en el intervalo [a, b].

    Args:
    - w: El valor en el intervalo [0, 1] que se desea convertir.
    - a, b: Los límites del intervalo objetivo [a, b].

    Returns:
    - float: El valor convertido en el intervalo [a, b].
    """
    return w * (b-a) + a

def _busquedaDorada(funcion, epsilon, a=None, b=None):
    """
    Implementa el método de búsqueda dorada para encontrar el mínimo de una función unidimensional.

    Args:
    - funcion (callable): La función objetivo que se desea minimizar.
    - epsilon (float): El criterio de convergencia. El algoritmo termina cuando el tamaño del intervalo es menor que epsilon.
    - a, b (float, opcional): Los límites del intervalo inicial de búsqueda. Por defecto, a=0.0 y b=1.0.

    Returns:
    - float: El punto que minimiza la función dentro del intervalo [a, b].
    """
    PHI = (1 + math.sqrt(5)) / 2 - 1
    aw, bw = 0, 1
    Lw = 1
    k = 1

    while Lw > epsilon:
        w2 = aw + PHI * Lw
        w1 = bw - PHI * Lw
        aw, bw = _regla_eliminacion(w1, w2, funcion(_w_to_x(w1, a, b)), 
                                    funcion(_w_to_x(w2, a, b)), aw, bw)
        k += 1
        Lw = bw - aw

    return (_w_to_x(aw, a, b) + _w_to_x(bw, a, b)) / 2

def gradiente(f, x, deltaX=0.00001):
    """
    Calcula el gradiente de una función f en un punto x utilizando el método de diferencia finita central.

    Args:
    - f (callable): La función objetivo para la cual se calcula el gradiente.
    - x (np.ndarray): El punto en el cual se evalúa el gradiente.
    - deltaX (float, opcional): El tamaño del paso para la diferencia finita central. Por defecto, deltaX=0.00001.

    Returns:
    - List[float]: Una lista de gradientes parciales en el punto x.
    """
    grad = []
    for i in range(0, len(x)):
        xp = x.copy()
        xn = x.copy()
        xp[i] = xp[i] + deltaX
        xn[i] = xn[i] - deltaX
        grad.append((f(xp) - f(xn)) / (2 * deltaX))
    return grad

def _hessian_matrix(f, x, deltaX=0.00001):
    """
    Calcula la matriz hessiana de una función f en un punto x utilizando el método de diferencia finita central.

    Args:
    - f (callable): La función objetivo para la cual se calcula la matriz hessiana.
    - x (np.ndarray): El punto en el cual se evalúa la matriz hessiana.
    - deltaX (float, opcional): El tamaño del paso para la diferencia finita central. Por defecto, deltaX=0.00001.

    Returns:
    - np.ndarray: La matriz hessiana evaluada en el punto x.
    """
    fx = f(x)
    N = len(x)
    H = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            if i == j:
                xp = x.copy()
                xn = x.copy()
                xp[i] = xp[i] + deltaX
                xn[i] = xn[i] - deltaX
                H[i, j] = (f(xp) - 2 * fx + f(xn)) / (deltaX ** 2)
            else:
                xpp = x.copy()
                xpn = x.copy()
                xnp = x.copy()
                xnn = x.copy()
                xpp[i] = xpp[i] + deltaX
                xpp[j] = xpp[j] + deltaX
                xpn[i] = xpn[i] + deltaX
                xpn[j] = xpn[j] - deltaX
                xnp[i] = xnp[i] - deltaX
                xnp[j] = xnp[j] + deltaX
                xnn[i] = xnn[i] - deltaX
                xnn[j] = xnn[j] - deltaX
                H[i, j] = (f(xpp) - f(xpn) - f(xnp) + f(xnn)) / (4 * deltaX ** 2)
    return H

def newton(funcion, x0, epsilon1, epsilon2, M):
    """
    Método de Newton para encontrar el mínimo de una función multidimensional.

    Args:
    - funcion (callable): La función objetivo que se desea minimizar.
    - x0 (np.ndarray): El punto inicial de la búsqueda.
    - epsilon1 (float): El criterio de convergencia para el gradiente. El algoritmo termina cuando el tamaño del gradiente es menor que epsilon1.
    - epsilon2 (float): El criterio de convergencia para la búsqueda unidireccional. El algoritmo termina cuando la distancia entre puntos sucesivos es menor que epsilon2.
    - M (int): El número máximo de iteraciones permitidas.

    Returns:
    - dict: Diccionario con los resultados de la optimización
        'punto_optimo': Punto óptimo encontrado
        'valor_optimo': Valor óptimo de la función en el punto óptimo
        'iteraciones': Número de iteraciones realizadas
        'trayectoria': Trayectoria de puntos visitados durante la optimización
    """
    terminar = False
    xk = x0
    k = 0
    trayectoria = [x0.tolist()]  # Inicializar la trayectoria con el punto inicial
    
    while not terminar:
        grad = np.array(gradiente(funcion, xk))
        hessiana = _hessian_matrix(funcion, xk)
        
        if np.linalg.norm(grad) < epsilon1 or k >= M:
            terminar = True
        else:
            def alpha_funcion(alpha):
                return funcion(xk - alpha * np.dot(np.linalg.inv(hessiana), grad))
            
            alpha = _busquedaDorada(alpha_funcion, epsilon=epsilon2, a=0.0, b=1.0)
            x_k1 = xk - alpha * np.dot(np.linalg.inv(hessiana), grad)
            trayectoria.append(x_k1.tolist())  # Guardar el punto visitado
            
            if np.linalg.norm(x_k1 - xk) / (np.linalg.norm(xk) + 0.00001) <= epsilon2:
                terminar = True
            else:
                k += 1
                xk = x_k1
    
    resultado = {
        'punto_optimo': xk,
        'valor_optimo': funcion(xk),
        'iteraciones': k,
        'trayectoria': trayectoria
    }
    
    return resultado