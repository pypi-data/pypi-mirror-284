import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def rosenbrock(x, y):
    """
    Función de Rosenbrock, definida matemáticamente como:
    f(x, y) = (1 - x)**2 + 100 * (y - x**2)**2
    
    Parámetros:
    ----------
    x : float or numpy.ndarray
        Primer componente de la función.
    y : float or numpy.ndarray
        Segundo componente de la función.

    Retorna:
    -------
    float or numpy.ndarray
        Valor de la función de Rosenbrock evaluada en (x, y).
    """
    return (1 - x)**2 + 100 * (y - x**2)**2

def rosenbrock_disk(x, y):
    """
    Función de Rosenbrock restringida a un disco de radio 2 centrado en el origen.

    Parámetros:
    ----------
    x : float or numpy.ndarray
        Primer componente de la función.
    y : float or numpy.ndarray
        Segundo componente de la función.

    Retorna:
    -------
    float or numpy.ndarray
        Valor de la función de Rosenbrock restringida al disco evaluada en (x, y).
    """
    return (1 - x)**2 + 100 * (y - x**2)**2

def bird_mishra(x, y):
    """
    Función de Bird-Mishra, definida matemáticamente como:
    f(x, y) = sin(y) * exp((1 - cos(x))**2) + cos(x) * exp((1 - sin(y))**2) + (x - y)**2
    
    Parámetros:
    ----------
    x : float or numpy.ndarray
        Primer componente de la función.
    y : float or numpy.ndarray
        Segundo componente de la función.

    Retorna:
    -------
    float or numpy.ndarray
        Valor de la función de Bird-Mishra evaluada en (x, y).
    """
    return np.sin(y) * np.exp((1 - np.cos(x))**2) + np.cos(x) * np.exp((1 - np.sin(y))**2) + (x - y)**2

def townsend(x, y):
    """
    Función de Townsend, definida matemáticamente como:
    f(x, y) = -(cos((x - 0.1) * y))^2 - x * sin(3 * x + y)

    Parámetros:
    ----------
    x : float or numpy.ndarray
        Primer componente de la función.
    y : float or numpy.ndarray
        Segundo componente de la función.

    Retorna:
    -------
    float or numpy.ndarray
        Valor de la función de Townsend evaluada en (x, y).
    """
    return (-(np.cos((x - 0.1) * y))**2) - (x * np.sin(3 * x + y))

def gomez_levy(x, y):
    """
    Función de Gómez y Levy, definida matemáticamente como:
    f(x, y) = 4*x**2 - 2.1*x**4 + (1/3)*x**6 + x*y - 4*y**2 + 4*y**4

    Parámetros:
    ----------
    x : float or numpy.ndarray
        Primer componente de la función.
    y : float or numpy.ndarray
        Segundo componente de la función.

    Retorna:
    -------
    float or numpy.ndarray
        Valor de la función de Gómez y Levy evaluada en (x, y).
    """
    return (4*x**2) - (2.1*x**4) + ((1/3)*x**6) + (x*y) - (4*y**2) + (4*y**4)

def simionescu(x, y):
    """
    Función de Simionescu, definida matemáticamente como:
    f(x, y) = 0.1 * (x * y)

    Parámetros:
    ----------
    x : float or numpy.ndarray
        Primer componente de la función.
    y : float or numpy.ndarray
        Segundo componente de la función.

    Retorna:
    -------
    float or numpy.ndarray
        Valor de la función de Simionescu evaluada en (x, y).
    """
    return 0.1 * (x * y)



def plot_rosenbrock_cubic_linear_constraint():
    """
    Genera un gráfico de contorno de la función de Rosenbrock, restringida por una cúbica y una restricción lineal.

    Utiliza una malla de puntos para evaluar la función de Rosenbrock y aplica restricciones cúbicas y lineales en el dominio.
    Muestra el punto óptimo conocido en el gráfico y configura etiquetas y título adecuados.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para las restricciones y el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    # Generar una malla de puntos
    x = np.linspace(-1.5, 1.5, 400)
    y = np.linspace(-0.5, 2.5, 400)
    X, Y = np.meshgrid(x, y)
    Z = rosenbrock(X, Y)

    # Definir las restricciones
    cubic_constraint = ((X - 1)**3) - Y + 1
    linear_constraint = X + Y - 2

    # Encontrar los puntos que satisfacen ambas restricciones
    inside_constraint = ((cubic_constraint <= 0)) & (linear_constraint <= 0)

    # Enmascarar los valores fuera de las restricciones
    Z_masked = np.ma.masked_where(~inside_constraint, Z)

    # Punto óptimo conocido
    optimal_point = [1.0, 1.0]

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    CS = ax.contourf(X, Y, Z_masked, levels=np.logspace(-3, 3, 20), cmap='viridis', norm=mcolors.LogNorm())
    ax.contour(X, Y, Z_masked, levels=np.logspace(-8, 8, 20), colors='white', alpha = 0.6)
    cbar = fig.colorbar(CS)

    # Graficar el punto óptimo
    ax.plot(optimal_point[0], optimal_point[1], 'ro', label='Punto óptimo')

    # Configurar límites de los ejes
    ax.set_xlim([-1.5, 1.1])
    ax.set_ylim([-0.5, 2.5])

    # Configurar etiquetas y título
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función de Rosenbrock restringida con una cúbica y una recta')
    ax.legend()

    # Mostrar el gráfico
    plt.show()

def plot_rosenbrock_disc_constraint():
    """
    Genera un gráfico de contorno de la función de Rosenbrock, restringida a un disco de radio 2 centrado en el origen.

    Utiliza una malla de puntos para evaluar la función de Rosenbrock y aplica una restricción circular en el dominio.
    Muestra el punto óptimo conocido en el gráfico y configura etiquetas y título adecuados.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para las restricciones y el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    # Generar una malla de puntos
    x = np.linspace(-1.5, 1.5, 400)
    y = np.linspace(-1.5, 1.5, 400)
    X, Y = np.meshgrid(x, y)
    Z = rosenbrock(X, Y)

    # Definir las restricciones (disco de radio 2 centrado en el origen)
    disc_constraint = (X**2) + (Y**2)

    # Encontrar los puntos que satisfacen la restricción
    inside_constraint = (disc_constraint <= 2)

    # Enmascarar los valores fuera de las restricciones
    Z_masked = np.ma.masked_where(~inside_constraint, Z)

    # Punto óptimo conocido
    optimal_point = [1.0, 1.0]

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    CS = ax.contourf(X, Y, Z_masked, levels=np.logspace(-3, 3, 20), cmap='viridis', norm=mcolors.LogNorm())
    ax.contour(X, Y, Z_masked, levels=np.logspace(-8, 8, 20), colors='white', alpha = 0.6)
    cbar = fig.colorbar(CS)

    # Graficar el punto óptimo
    ax.plot(optimal_point[0], optimal_point[1], 'ro', label='Punto óptimo')

    # Configurar límites de los ejes
    ax.set_xlim([-1.5, 1.5])
    ax.set_ylim([-1.5, 1.5])

    # Configurar etiquetas y título
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función de Rosenbrock restringida a un disco')
    ax.legend()

    # Mostrar el gráfico
    plt.show()

def plot_bird_mishra_with_constraints():
    """
    Genera un gráfico de contorno de la función de Bird-Mishra, restringida por una condición circular.

    Utiliza una malla de puntos para evaluar la función de Bird-Mishra y aplica una restricción circular en el dominio.
    Muestra el punto óptimo conocido en el gráfico y configura etiquetas y título adecuados.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para las restricciones y el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """

    # Generar una malla de puntos
    x = np.linspace(-10, 0, 400)
    y = np.linspace(-10, 0, 400)
    X, Y = np.meshgrid(x, y)
    Z = bird_mishra(X, Y)

    # Definir las restricciones (círculo de radio 5 centrado en (-5, -5))
    constraint1 = (X + 5)**2 + (Y + 5)**2

    # Encontrar los puntos que satisfacen la restricción
    inside_constraint = (constraint1 < 25)

    # Enmascarar los valores fuera de las restricciones
    Z_masked = np.ma.masked_where(~inside_constraint, Z)

    # Punto óptimo conocido
    optimal_point = [-3.1302468, -1.5821422]

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z_masked, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z_masked, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    # Graficar el punto óptimo
    ax.plot(optimal_point[0], optimal_point[1], 'ro', label='Punto óptimo')

    # Configurar límites de los ejes
    ax.set_xlim([-10, 0])
    ax.set_ylim([-10, 0])

    # Configurar etiquetas y título
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Función Bird de Mishra con restricciones')
    ax.legend()

    # Mostrar el gráfico
    plt.show()

def plot_townsend_with_constraints():
    """
    Genera un gráfico de contorno de la función de Townsend con restricciones definidas.

    Utiliza una malla de puntos para evaluar la función de Townsend y aplica restricciones en el dominio.
    Configura etiquetas y título adecuados.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para las restricciones y el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    # Generar una malla de puntos
    x = np.linspace(-2.25, 2.25, 400)
    y = np.linspace(-2.5, 1.75, 400)
    X, Y = np.meshgrid(x, y)
    Z = townsend(X, Y)

    # Aplicar las restricciones directamente en el código
    t = np.arctan2(Y, X)
    left_side = X**2 + Y**2
    right_side = (2 * np.cos(t) - 0.5 * np.cos(2*t) - 0.25 * np.cos(3*t) - 0.125 * np.cos(4*t))**2 + (2 * np.sin(t))**2
    inside_constraint = left_side < right_side

    # Enmascarar los valores fuera de las restricciones
    Z_masked = np.ma.masked_where(~inside_constraint, Z)

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z_masked, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z_masked, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    # Configurar límites de los ejes
    ax.set_xlim([-2.25, 2.25])
    ax.set_ylim([-2.5, 1.75])

    # Configurar etiquetas y título
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Gráfica de la función de Townsend con restricciones')

    # Mostrar el gráfico
    plt.show()

def plot_gomez_levy_with_constraints():
    """
    Genera un gráfico de contorno de la función de Gomez y Levy con restricciones definidas.

    Utiliza una malla de puntos para evaluar la función de Gomez y Levy y aplica restricciones en el dominio.
    Configura etiquetas y título adecuados.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para las restricciones y el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """
    # Generar una malla de puntos
    x = np.linspace(-1, 0.75, 400)
    y = np.linspace(-1, 1, 400)
    X, Y = np.meshgrid(x, y)
    Z = gomez_levy(X, Y)

    # Aplicar las restricciones directamente en el código
    inside_constraint = (-np.sin(4*np.pi*X) + 2*np.sin(2*np.pi*Y)**2) <= 1.5

    # Enmascarar los valores fuera de las restricciones
    Z_masked = np.ma.masked_where(~inside_constraint, Z)

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z_masked, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z_masked, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    # Configurar límites de los ejes
    ax.set_xlim([-1, 0.75])
    ax.set_ylim([-1, 1])

    # Configurar etiquetas y título
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Gráfica de la función de Gomez y Levy con restricciones')

    # Mostrar el gráfico
    plt.show()

def plot_simionescu_with_constraints():
    """
    Genera un gráfico de contorno de la función de Simionescu con restricciones definidas.

    Utiliza una malla de puntos para evaluar la función de Simionescu y aplica restricciones en el dominio.
    Configura etiquetas y título adecuados.

    Parámetros:
    ----------
    No recibe parámetros de entrada directos. Utiliza valores predefinidos para las restricciones y el tamaño del gráfico.

    Retorna:
    -------
    None
        Muestra el gráfico utilizando matplotlib.
    """

    # Generar una malla de puntos
    x = np.linspace(-1.25, 1.25, 400)
    y = np.linspace(-1.25, 1.25, 400)
    X, Y = np.meshgrid(x, y)
    Z = simionescu(X, Y)

    # Definir los parámetros de la restricción
    r_T = 1
    r_S = 0.2
    n = 8

    # Aplicar las restricciones directamente en el código
    theta = np.arctan2(Y, X)
    left_side = X**2 + Y**2
    right_side = (r_T + r_S * np.cos(n * theta))**2
    inside_constraint = left_side <= right_side

    # Enmascarar los valores fuera de las restricciones
    Z_masked = np.ma.masked_where(~inside_constraint, Z)

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    levels = np.linspace(np.min(Z), np.max(Z), 20)
    CS = ax.contourf(X, Y, Z_masked, levels=levels, cmap='viridis')
    ax.contour(X, Y, Z_masked, levels=levels, colors='white')
    cbar = fig.colorbar(CS)

    # Configurar límites de los ejes
    ax.set_xlim([-1.25, 1.25])
    ax.set_ylim([-1.25, 1.25])

    # Configurar etiquetas y título
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_title('Gráfica de la función de Simionescu con restricciones')

    # Mostrar el gráfico
    plt.show()