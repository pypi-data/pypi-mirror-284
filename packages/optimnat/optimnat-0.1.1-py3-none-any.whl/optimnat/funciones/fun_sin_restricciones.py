import numpy as np
import matplotlib.pyplot as plt

def rastrigin(x, y, A=10, n=2):
    """
    Función de Rastrigin en dos dimensiones.

    Parámetros:
    -----------
    x : float
        Valor en el eje x.
    y : float
        Valor en el eje y.
    A : float, opcional
        Parámetro de ajuste (por defecto A=10).
    n : int, opcional
        Dimensión de la función (por defecto n=2).

    Retorna:
    --------
    float
        Valor de la función de Rastrigin en (x, y).
    """
    return A * n + (x**2 - A * np.cos(2 * np.pi * x)) + (y**2 - A * np.cos(2 * np.pi * y))


def plot_rastrigin():
    """
    Genera un gráfico de contorno de la función de Rastrigin en dos dimensiones.

    Utiliza una malla de puntos para evaluar la función de Rastrigin y configura etiquetas y título adecuados.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    # Generar una malla de puntos
    x = np.linspace(-5.12, 5.12, 400)
    y = np.linspace(-5.12, 5.12, 400)
    X, Y = np.meshgrid(x, y)
    Z = rastrigin(X, Y)

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    # Configurar límites de los ejes
    ax.set_xlim([-5.12, 5.12])
    ax.set_ylim([-5.12, 5.12])

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función de Rastrigin')
    ax.legend()

    plt.show()

def ackley(x, y, a=20, b=0.2, c=2*np.pi):
    """
    Función de Ackley en dos dimensiones.

    Parámetros:
    ----------
    x : float
        Valor en el eje x.
    y : float
        Valor en el eje y.
    a : float, opcional
        Parámetro de la función. Por defecto es 20.
    b : float, opcional
        Parámetro de la función. Por defecto es 0.2.
    c : float, opcional
        Parámetro de la función. Por defecto es 2 * pi.

    Retorna:
    -------
    float
        Valor de la función de Ackley evaluada en (x, y).
    """
    sum_sq_term = -b * np.sqrt(0.5 * (x**2 + y**2))
    cos_term = 0.5 * (np.cos(c * x) + np.cos(c * y))
    return -a * np.exp(sum_sq_term) - np.exp(cos_term) + a + np.exp(1)

def plot_ackley():
    """
    Genera un gráfico de contorno de la función de Ackley sin restricciones.

    Utiliza una malla de puntos para evaluar la función de Ackley y muestra el gráfico.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    # Generar una malla de puntos
    x = np.linspace(-5, 5, 400)
    y = np.linspace(-5, 5, 400)
    X, Y = np.meshgrid(x, y)
    Z = ackley(X, Y)

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    # Configurar límites de los ejes
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Gráfica de la función de Ackley')

    plt.show()

def sphere(x, y):
    """
    Función esférica, definida matemáticamente como:
    f(x, y) = x^2 + y^2

    Parámetros:
    ----------
    x : float or numpy.ndarray
        Primer componente de la función.
    y : float or numpy.ndarray
        Segundo componente de la función.

    Retorna:
    -------
    float or numpy.ndarray
        Valor de la función esférica evaluada en (x, y).
    """
    return x**2 + y**2

def plot_sphere():
    """
    Genera un gráfico de contorno de la función esférica sin restricciones.

    Utiliza una malla de puntos para evaluar la función esférica y muestra el gráfico.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    # Generar una malla de puntos
    x = np.linspace(-5, 5, 400)
    y = np.linspace(-5, 5, 400)
    X, Y = np.meshgrid(x, y)
    Z = sphere(X, Y)

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    # Configurar límites de los ejes
    ax.set_xlim([-5, 5])
    ax.set_ylim([-5, 5])

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Gráfica de la función esférica')
    plt.show()

def rosenbrock(x, y, a=1, b=100):
    """
    Función de Rosenbrock, definida matemáticamente como:
    f(x, y) = (a - x)^2 + b * (y - x^2)^2

    Parámetros:
    ----------
    x : float or numpy.ndarray
        Primer componente de la función.
    y : float or numpy.ndarray
        Segundo componente de la función.
    a : float, opcional
        Parámetro de la función. Por defecto es 1.
    b : float, opcional
        Parámetro de la función. Por defecto es 100.

    Retorna:
    -------
    float or numpy.ndarray
        Valor de la función de Rosenbrock evaluada en (x, y).
    """
    return (a - x)**2 + b * (y - x**2)**2

def plot_rosenbrock():
    """
    Genera un gráfico de contorno de la función de Rosenbrock sin restricciones.

    Utiliza una malla de puntos para evaluar la función de Rosenbrock y muestra el gráfico.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    # Generar una malla de puntos
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-2, 2, 400)
    X, Y = np.meshgrid(x, y)
    Z = rosenbrock(X, Y)

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 50)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    # Configurar límites de los ejes
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Gráfica de la función de Rosenbrock')

    plt.show()

def beale(x, y):
    """
    Función de Beale, definida matemáticamente como:
    f(x, y) = (1.5 - x + x*y)^2 + (2.25 - x + x*y^2)^2 + (2.625 - x + x*y^3)^2

    Parámetros:
    ----------
    x : float or numpy.ndarray
        Primer componente de la función.
    y : float or numpy.ndarray
        Segundo componente de la función.

    Retorna:
    -------
    float or numpy.ndarray
        Valor de la función de Beale evaluada en (x, y).
    """
    return (1.5 - x + x * y)**2 + (2.25 - x + x * y**2)**2 + (2.625 - x + x * y**3)**2

def plot_beale():
    """
    Genera un gráfico de contorno de la función de Beale sin restricciones.

    Utiliza una malla de puntos para evaluar la función de Beale y muestra el gráfico.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    # Generar una malla de puntos
    x = np.linspace(-4.5, 4.5, 400)
    y = np.linspace(-4.5, 4.5, 400)
    X, Y = np.meshgrid(x, y)
    Z = beale(X, Y)

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 50)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    # Configurar límites de los ejes
    ax.set_xlim([-4.5, 4.5])
    ax.set_ylim([-4.5, 4.5])

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Gráfica de la función de Beale')

    plt.show()

def goldstein_price(x, y):
    """
    Función de Goldstein-Price, definida matemáticamente como:
    f(x, y) = [1 + (x + y + 1)^2 * (19 - 14*x + 3*x^2 - 14*y + 6*x*y + 3*y^2)] *
              [30 + (2*x - 3*y)^2 * (18 - 32*x + 12*x^2 + 48*y - 36*x*y + 27*y^2)]

    Parámetros:
    ----------
    x : float or numpy.ndarray
        Primer componente de la función.
    y : float or numpy.ndarray
        Segundo componente de la función.

    Retorna:
    -------
    float or numpy.ndarray
        Valor de la función de Goldstein-Price evaluada en (x, y).
    """
    part1 = (1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2))
    part2 = (30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2))
    return part1 * part2

def plot_goldstein_price():
    """
    Genera un gráfico de contorno de la función de Goldstein-Price sin restricciones.

    Utiliza una malla de puntos para evaluar la función de Goldstein-Price y muestra el gráfico de contorno.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    x = np.linspace(-2, 2, 400)
    y = np.linspace(-2, 2, 400)
    X, Y = np.meshgrid(x, y)
    Z = goldstein_price(X, Y)

    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función de Goldstein-Price')
    plt.show()

def booth(x, y):
    """
    Función de Booth, definida matemáticamente como:
    f(x, y) = (x + 2*y - 7)^2 + (2*x + y - 5)^2

    Parámetros:
    ----------
    x : float or numpy.ndarray
        Primer componente de la función.
    y : float or numpy.ndarray
        Segundo componente de la función.

    Retorna:
    -------
    float or numpy.ndarray
        Valor de la función de Booth evaluada en (x, y).
    """
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2

def plot_booth():
    """
    Genera un gráfico de contorno de la función de Booth sin restricciones.

    Utiliza una malla de puntos para evaluar la función de Booth y muestra el gráfico de contorno.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)
    Z = booth(X, Y)

    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función de Booth')

    plt.show()

def bukin_n6(x, y):
    """
    Función de Bukin N.6, definida matemáticamente como:
    f(x, y) = 100 * sqrt(|y - 0.01*x^2|) + 0.01 * |x + 10|

    Parámetros:
    ----------
    x : float or numpy.ndarray
        Primer componente de la función.
    y : float or numpy.ndarray
        Segundo componente de la función.

    Retorna:
    -------
    float or numpy.ndarray
        Valor de la función de Bukin N.6 evaluada en (x, y).
    """
    return 100 * np.sqrt(np.abs(y - 0.01*x**2)) + 0.01 * np.abs(x + 10)

def plot_bukin_n6():
    """
    Genera un gráfico de contorno de la función de Bukin N.6 sin restricciones.

    Utiliza una malla de puntos para evaluar la función de Bukin N.6 y muestra el gráfico de contorno.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    x = np.linspace(-15, -5, 400)
    y = np.linspace(-3, 3, 400)
    X, Y = np.meshgrid(x, y)
    Z = bukin_n6(X, Y)

    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función de Bukin N.6')

    plt.show()

def matyas(x, y):
    """
    Función de Matyas, definida matemáticamente como:
    f(x, y) = 0.26 * (x^2 + y^2) - 0.48 * x * y

    Parámetros:
    ----------
    x : float or numpy.ndarray
        Primer componente de la función.
    y : float or numpy.ndarray
        Segundo componente de la función.

    Retorna:
    -------
    float or numpy.ndarray
        Valor de la función de Matyas evaluada en (x, y).
    """
    return 0.26 * (x**2 + y**2) - 0.48 * x * y

def plot_matyas():
    """
    Genera un gráfico de contorno de la función de Matyas sin restricciones.

    Utiliza una malla de puntos para evaluar la función de Matyas y muestra el gráfico de contorno.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)
    Z = matyas(X, Y)

    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función de Matyas')

    plt.show()

def levi_n13(x, y):
    """
    Función de Lévi N.13, definida matemáticamente como:
    f(x, y) = sin^2(3 * pi * x) + (x - 1)^2 * (1 + sin^2(3 * pi * y)) + (y - 1)^2 * (1 + sin^2(2 * pi * y))

    Parámetros:
    ----------
    x : float or numpy.ndarray
        Primer componente de la función.
    y : float or numpy.ndarray
        Segundo componente de la función.

    Retorna:
    -------
    float or numpy.ndarray
        Valor de la función de Lévi N.13 evaluada en (x, y).
    """
    return np.sin(3 * np.pi * x)**2 + (x - 1)**2 * (1 + np.sin(3 * np.pi * y)**2) + (y - 1)**2 * (1 + np.sin(2 * np.pi * y)**2)

def plot_levi_n13():
    """
    Genera un gráfico de contorno de la función de Lévi N.13 sin restricciones.

    Utiliza una malla de puntos para evaluar la función de Lévi N.13 y muestra el gráfico de contorno.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)
    Z = levi_n13(X, Y)

    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función de Lévi N.13')

    plt.show()

def himmelblau(x, y):
    """
    Función de Himmelblau, definida matemáticamente como:
    f(x, y) = (x^2 + y - 11)^2 + (x + y^2 - 7)^2

    Parámetros:
    ----------
    x : float or numpy.ndarray
        Primer componente de la función.
    y : float or numpy.ndarray
        Segundo componente de la función.

    Retorna:
    -------
    float or numpy.ndarray
        Valor de la función de Himmelblau evaluada en (x, y).
    """
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

def plot_himmelblau():
    """
    Genera un gráfico de contorno de la función de Himmelblau sin restricciones.

    Utiliza una malla de puntos para evaluar la función de Himmelblau y muestra el gráfico de contorno.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    x = np.linspace(-5, 5, 400)
    y = np.linspace(-5, 5, 400)
    X, Y = np.meshgrid(x, y)
    Z = himmelblau(X, Y)

    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función de Himmelblau')

    plt.show()

def three_hump_camel(x, y):
    """
    Función de Three-hump Camel, definida matemáticamente como:
    f(x, y) = 2*x^2 - 1.05*x^4 + (x^6)/6 + x*y + y^2

    Parámetros:
    ----------
    x : float or numpy.ndarray
        Primer componente de la función.
    y : float or numpy.ndarray
        Segundo componente de la función.

    Retorna:
    -------
    float or numpy.ndarray
        Valor de la función de Three-hump Camel evaluada en (x, y).
    """
    return 2*x**2 - 1.05*x**4 + (x**6)/6 + x*y + y**2

def plot_three_hump_camel():
    """
    Genera un gráfico de contorno de la función de Three-hump Camel sin restricciones.

    Utiliza una malla de puntos para evaluar la función de Three-hump Camel y muestra el gráfico de contorno.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    x = np.linspace(-5, 5, 400)
    y = np.linspace(-5, 5, 400)
    X, Y = np.meshgrid(x, y)
    Z = three_hump_camel(X, Y)

    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función de Three-hump Camel')

    plt.show()

def easom(x, y):
    """
    Función de Easom, definida matemáticamente como:
    f(x, y) = -cos(x) * cos(y) * exp(-((x - pi)^2 + (y - pi)^2))

    Parámetros:
    ----------
    x : float or numpy.ndarray
        Primer componente de la función.
    y : float or numpy.ndarray
        Segundo componente de la función.

    Retorna:
    -------
    float or numpy.ndarray
        Valor de la función de Easom evaluada en (x, y).
    """
    return -np.cos(x) * np.cos(y) * np.exp(-((x - np.pi)**2 + (y - np.pi)**2))

def plot_easom():
    """
    Genera un gráfico de contorno de la función de Easom sin restricciones.

    Utiliza una malla de puntos para evaluar la función de Easom y muestra el gráfico de contorno.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    x = np.linspace(-100, 100, 400)
    y = np.linspace(-100, 100, 400)
    X, Y = np.meshgrid(x, y)
    Z = easom(X, Y)

    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función de Easom')

    plt.show()

def cross_in_tray(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Calcula el valor de la función de Cross-in-Tray para los valores dados de x e y.

    Parameters:
    -----------
    x : np.ndarray
        Arreglo de valores de coordenadas x.
    y : np.ndarray
        Arreglo de valores de coordenadas y.

    Returns:
    --------
    np.ndarray
        Arreglo con los valores de la función evaluada en cada par (x, y).
    """
    return -0.0001 * (np.abs(np.sin(x) * np.sin(y) * np.exp(np.abs(100 - np.sqrt(x**2 + y**2) / np.pi))) + 1)**0.1

def plot_cross_in_tray():
    """
    Genera un gráfico de contorno de la función de Cross-in-Tray.

    Utiliza una malla de puntos para evaluar la función de Cross-in-Tray y muestra el gráfico de contorno.

    Returns:
    --------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)
    Z = cross_in_tray(X, Y)

    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función de Cross-in-Tray')

    plt.show()

def eggholder(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Calcula el valor de la función Eggholder para los valores dados de x e y.

    Parameters:
    -----------
    x : np.ndarray
        Arreglo de valores de coordenadas x.
    y : np.ndarray
        Arreglo de valores de coordenadas y.

    Returns:
    --------
    np.ndarray
        Arreglo con los valores de la función evaluada en cada par (x, y).
    """
    return -(y + 47) * np.sin(np.sqrt(np.abs(x/2 + (y + 47)))) - x * np.sin(np.sqrt(np.abs(x - (y + 47))))

def plot_eggholder():
    """
    Genera un gráfico de contorno de la función de Eggholder.

    Utiliza una malla de puntos para evaluar la función de Eggholder y muestra el gráfico de contorno.

    Returns:
    --------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    x = np.linspace(-512, 512, 400)
    y = np.linspace(-512, 512, 400)
    X, Y = np.meshgrid(x, y)
    Z = eggholder(X, Y)

    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función de Eggholder')

    plt.show()

def holder_table(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Calcula el valor de la función Holder Table para los valores dados de x e y.

    Parameters:
    -----------
    x : np.ndarray
        Arreglo de valores de coordenadas x.
    y : np.ndarray
        Arreglo de valores de coordenadas y.

    Returns:
    --------
    np.ndarray
        Arreglo con los valores de la función evaluada en cada par (x, y).
    """
    return -np.abs(np.sin(x) * np.cos(y) * np.exp(np.abs(1 - np.sqrt(x**2 + y**2) / np.pi)))

def plot_holder_table():
    """
    Genera un gráfico de contorno de la función de Holder Table.

    Utiliza una malla de puntos para evaluar la función de Holder Table y muestra el gráfico de contorno.

    Returns:
    --------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)
    Z = holder_table(X, Y)

    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función de Hölder Table')

    plt.show()

def mccormick(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Calcula el valor de la función de McCormick para los valores dados de x e y.

    Parameters:
    -----------
    x : np.ndarray
        Arreglo de valores de coordenadas x.
    y : np.ndarray
        Arreglo de valores de coordenadas y.

    Returns:
    --------
    np.ndarray
        Arreglo con los valores de la función evaluada en cada par (x, y).
    """
    return np.sin(x + y) + (x - y)**2 - 1.5*x + 2.5*y + 1

def plot_mccormick():
    """
    Genera un gráfico de contorno de la función de McCormick.

    Utiliza una malla de puntos para evaluar la función de McCormick y muestra el gráfico de contorno.

    Returns:
    --------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    x = np.linspace(-1.5, 4, 400)
    y = np.linspace(-3, 4, 400)
    X, Y = np.meshgrid(x, y)
    Z = mccormick(X, Y)

    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función de McCormick')

    plt.show()

def schaffer_n2(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Calcula el valor de la función Schaffer N. 2 para los valores dados de x e y.

    Parameters:
    -----------
    x : np.ndarray
        Arreglo de valores de coordenadas x.
    y : np.ndarray
        Arreglo de valores de coordenadas y.

    Returns:
    --------
    np.ndarray
        Arreglo con los valores de la función evaluada en cada par (x, y).
    """
    return 0.5 + (np.sin(x**2 - y**2)**2 - 0.5) / (1 + 0.001 * (x**2 + y**2))**2

def plot_schaffer_n2():
    """
    Genera un gráfico de contorno de la función de Schaffer N. 2.

    Utiliza una malla de puntos para evaluar la función de Schaffer N. 2 y muestra el gráfico de contorno.

    Returns:
    --------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    x = np.linspace(-100, 100, 400)
    y = np.linspace(-100, 100, 400)
    X, Y = np.meshgrid(x, y)
    Z = schaffer_n2(X, Y)

    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función de Schaffer N. 2')

    plt.show()

def schaffer_n4(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Calcula el valor de la función Schaffer N. 4 para los valores dados de x e y.

    Parameters:
    -----------
    x : np.ndarray
        Arreglo de valores de coordenadas x.
    y : np.ndarray
        Arreglo de valores de coordenadas y.

    Returns:
    --------
    np.ndarray
        Arreglo con los valores de la función evaluada en cada par (x, y).
    """
    return 0.5 + (np.cos(np.sin(np.abs(x**2 - y**2)))**2 - 0.5) / (1 + 0.001 * (x**2 + y**2))**2

def plot_schaffer_n4():
    """
    Genera un gráfico de contorno de la función de Schaffer N. 4.

    Utiliza una malla de puntos para evaluar la función de Schaffer N. 4 y muestra el gráfico de contorno.

    Returns:
    --------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    x = np.linspace(-100, 100, 400)
    y = np.linspace(-100, 100, 400)
    X, Y = np.meshgrid(x, y)
    Z = schaffer_n4(X, Y)

    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función de Schaffer N. 4')

    plt.show()

def styblinski_tang(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """
    Calcula el valor de la función Styblinski-Tang para los valores dados de x e y.

    Parameters:
    -----------
    x : np.ndarray
        Arreglo de valores de coordenadas x.
    y : np.ndarray
        Arreglo de valores de coordenadas y.

    Returns:
    --------
    np.ndarray
        Arreglo con los valores de la función evaluada en cada par (x, y).
    """
    return 0.5 * ((x**4 - 16 * x**2 + 5 * x) + (y**4 - 16 * y**2 + 5 * y))

def plot_styblinski_tang():
    """
    Genera un gráfico de contorno de la función de Styblinski-Tang.

    Utiliza una malla de puntos para evaluar la función de Styblinski-Tang y muestra el gráfico de contorno.

    Returns:
    --------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    x = np.linspace(-5, 5, 400)
    y = np.linspace(-5, 5, 400)
    X, Y = np.meshgrid(x, y)
    Z = styblinski_tang(X, Y)

    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función de Styblinski-Tang')

    plt.show()

def shekel(X: np.ndarray, m: int = 10) -> np.ndarray:
    """
    Calcula el valor de la función de Shekel para los valores dados de x e y.

    Parameters:
    -----------
    X : np.ndarray
        Arreglo de valores de coordenadas x e y.
    m : int, opcional
        Número de términos en la suma (por defecto es 10).

    Returns:
    --------
    np.ndarray
        Arreglo con los valores de la función evaluada en cada par (x, y).
    """
    a = np.array([[4, 4, 4, 4],
                  [1, 1, 1, 1],
                  [8, 8, 8, 8],
                  [6, 6, 6, 6],
                  [3, 7, 3, 7],
                  [2, 9, 2, 9],
                  [5, 5, 3, 3],
                  [8, 1, 8, 1],
                  [6, 2, 6, 2],
                  [7, 3.6, 7, 3.6]])
    c = np.array([0.1, 0.2, 0.2, 0.4, 0.4, 0.6, 0.3, 0.7, 0.5, 0.5])
    
    s = np.zeros(X.shape[0])
    for i in range(m):
        s += 1 / (np.sum((X - a[i, :])**2, axis=1) + c[i])
    return -s

def plot_shekel():
    """
    Genera un gráfico de superficie de la función de Shekel.

    Utiliza una malla de puntos para evaluar la función de Shekel y muestra el gráfico de superficie.

    Returns:
    --------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    x = np.linspace(0, 10, 400)
    y = np.linspace(0, 10, 400)
    X, Y = np.meshgrid(x, y)
    XY = np.stack([X.ravel(), Y.ravel()]).T
    Z = shekel(XY).reshape(X.shape)

    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')
    ax.set_title('Función de Shekel')

    plt.show()
