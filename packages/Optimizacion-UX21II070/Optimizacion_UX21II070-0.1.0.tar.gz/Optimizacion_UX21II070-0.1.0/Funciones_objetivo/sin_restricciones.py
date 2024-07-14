"""
Módulo de funciones de prueba para algoritmos de optimización
=============================================================

Este módulo define varias funciones matemáticas utilizadas en optimización,
así como métodos para graficar estas funciones en 3D.

Funciones
---------
- `rastrigin(x)`: Función de Rastrigin, conocida por su paisaje con múltiples óptimos locales.
- `ackley(x, y=1)`: Función de Ackley, una función multimodal con un único óptimo global.
- `sphere(x)`: Función de Esfera, una función unimodal con un único óptimo global.
- `rosenbrock(x)`: Función de Rosenbrock, utilizada para probar algoritmos de optimización en problemas de minimización no lineales.
- `beale(x, y=1)`: Función de Beale, un problema de optimización no lineal con un óptimo global.
- `goldstein_price(x, y=1)`: Función de Goldstein-Price, una función con varios óptimos locales y globales.
- `booth(x, y=1)`: Función de Booth, una función de prueba simple para problemas de optimización.
- `bukin_n6(x, y=1)`: Función Bukin N.6, un problema de prueba con un paisaje de optimización desafiante.
- `matyas(x, y=1)`: Función de Matyas, una función multimodal con un óptimo global.
- `levi_n13(x, y=1)`: Función Levi N.13, una función de prueba con un paisaje de múltiples óptimos.
- `himmelblau(x, y=1)`: Función de Himmelblau, una función de prueba con múltiples óptimos locales y globales.
- `camello_tres_jorobas(x, y=1)`: Función del Camello de Tres Jorobas, un problema de prueba con un paisaje de optimización complejo.
- `easom(x, y=1)`: Función de Easom, un problema de optimización con un único óptimo global.
- `cross_in_tray(x, y=1)`: Función Cross-in-Tray, una función de prueba con un paisaje complicado para algoritmos de optimización.

Métodos
-------
- `graficar_funcion(funcion, rango_x, rango_y, titulo)`: Grafica una función matemática en 3D para un rango dado de valores en las dimensiones x e y.
- `graficar(funcion_nombre)`: Selecciona y grafica una función matemática predefinida en 3D usando el nombre de la función.

Ejemplos
--------
Para graficar la función de Rastrigin en el rango [-5.12, 5.12] para ambas dimensiones:

    graficar("Rastrigin")
"""


import numpy as np
import matplotlib.pyplot as plt

def rastrigin(x):
    """
    Función de Rastrigin.

    Parámetros
    ----------
    x : array-like
        Arreglo de entrada.

    Retorna
    -------
    float
        Valor de salida de la función de Rastrigin.
    """
    x = np.array(x)
    return 10 * len(x) + np.sum(x**2 - 10 * np.cos(2 * np.pi * x))

def ackley(x, y=1):
    """
    Función de Ackley.

    Parámetros
    ----------
    x : float
        Valor de entrada para la dimensión x.
    y : float, opcional
        Valor de entrada para la dimensión y (por defecto es 1).

    Retorna
    -------
    float
        Valor de salida de la función de Ackley.
    """
    return -20 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + np.e + 20

def sphere(x):
    """
    Función de Esfera.

    Parámetros
    ----------
    x : array-like
        Arreglo de entrada.

    Retorna
    -------
    float
        Valor de salida de la función de Esfera.
    """
    return sum(np.array(x)**2)

def rosenbrock(x):
    """
    Función de Rosenbrock.

    Parámetros
    ----------
    x : array-like
        Arreglo de entrada.

    Retorna
    -------
    float
        Valor de salida de la función de Rosenbrock.
    """
    x = np.array(x)
    return np.sum(100*(x[1:] - x[:-1]**2)**2 + (1 - x[:-1])**2)

def beale(x, y=1):
    """
    Función de Beale.

    Parámetros
    ----------
    x : float
        Valor de entrada para la dimensión x.
    y : float, opcional
        Valor de entrada para la dimensión y (por defecto es 1).

    Retorna
    -------
    float
        Valor de salida de la función de Beale.
    """
    return (1.5 - x + x * y)**2 + (2.25 - x + x * y**2)**2 + (2.625 - x + x * y**3)**2

def goldstein_price(x, y=1):
    """
    Función de Goldstein-Price.

    Parámetros
    ----------
    x : float
        Valor de entrada para la dimensión x.
    y : float, opcional
        Valor de entrada para la dimensión y (por defecto es 1).

    Retorna
    -------
    float
        Valor de salida de la función de Goldstein-Price.
    """
    return (1 + (x + y + 1)**2 * (19 - 14*x + 3*x**2 - 14*y + 6*x*y + 3*y**2)) * (30 + (2*x - 3*y)**2 * (18 - 32*x + 12*x**2 + 48*y - 36*x*y + 27*y**2))

def booth(x, y=1):
    """
    Función de Booth.

    Parámetros
    ----------
    x : float
        Valor de entrada para la dimensión x.
    y : float, opcional
        Valor de entrada para la dimensión y (por defecto es 1).

    Retorna
    -------
    float
        Valor de salida de la función de Booth.
    """
    return (x + 2*y - 7)**2 + (2*x + y - 5)**2

def bukin_n6(x, y=1):
    """
    Función Bukin N.6.

    Parámetros
    ----------
    x : float
        Valor de entrada para la dimensión x.
    y : float, opcional
        Valor de entrada para la dimensión y (por defecto es 1).

    Retorna
    -------
    float
        Valor de salida de la función Bukin N.6.
    """
    return 100 * np.sqrt(np.abs(y - 0.01*x**2)) + 0.01 * np.abs(x + 10)

def matyas(x, y=1):
    """
    Función de Matyas.

    Parámetros
    ----------
    x : float
        Valor de entrada para la dimensión x.
    y : float, opcional
        Valor de entrada para la dimensión y (por defecto es 1).

    Retorna
    -------
    float
        Valor de salida de la función de Matyas.
    """
    return 0.26 * (x**2 + y**2) - 0.48 * x * y

def levi_n13(x, y=1):
    """
    Función Levi N.13.

    Parámetros
    ----------
    x : float
        Valor de entrada para la dimensión x.
    y : float, opcional
        Valor de entrada para la dimensión y (por defecto es 1).

    Retorna
    -------
    float
        Valor de salida de la función Levi N.13.
    """
    return np.sin(3 * np.pi * x)**2 + (x - 1)**2 * (1 + np.sin(3 * np.pi * y)**2) + (y - 1)**2 * (1 + np.sin(2 * np.pi * y)**2)

def himmelblau(x, y=1):
    """
    Función de Himmelblau.

    Parámetros
    ----------
    x : float
        Valor de entrada para la dimensión x.
    y : float, opcional
        Valor de entrada para la dimensión y (por defecto es 1).

    Retorna
    -------
    float
        Valor de salida de la función de Himmelblau.
    """
    return (x**2 + y - 11)**2 + (x + y**2 - 7)**2

def camello_tres_jorobas(x, y=1):
    """
    Función del Camello de Tres Jorobas.

    Parámetros
    ----------
    x : float
        Valor de entrada para la dimensión x.
    y : float, opcional
        Valor de entrada para la dimensión y (por defecto es 1).

    Retorna
    -------
    float
        Valor de salida de la función del Camello de Tres Jorobas.
    """
    return 2*x**2 - 1.05*x**4 + (x**6)/6 + x*y + y**2

def easom(x, y=1):
    """
    Función de Easom.

    Parámetros
    ----------
    x : float
        Valor de entrada para la dimensión x.
    y : float, opcional
        Valor de entrada para la dimensión y (por defecto es 1).

    Retorna
    -------
    float
        Valor de salida de la función de Easom.
    """
    return -np.cos(x) * np.cos(y) * np.exp(-((x - np.pi)**2 + (y - np.pi)**2))

def cross_in_tray(x, y=1):
    """
    Función Cross-in-Tray.

    Parámetros
    ----------
    x : float
        Valor de entrada para la dimensión x.
    y : float, opcional
        Valor de entrada para la dimensión y (por defecto es 1).

    Retorna
    -------
    float
        Valor de salida de la función Cross-in-Tray.
    """
    return -0.0001 * (np.abs(np.sin(x) * np.sin(y) * np.exp(np.abs(100 - np.sqrt(x**2 + y**2) / np.pi))) + 1)**0.1

def graficar_funcion(funcion, rango_x, rango_y, titulo):
    """
    Grafica una función en un rango dado.

    Parámetros
    ----------
    funcion : callable
        La función a graficar.
    rango_x : list
        El rango de valores para la dimensión x.
    rango_y : list
        El rango de valores para la dimensión y.
    titulo : str
        El título del gráfico.

    Retorna
    -------
    None
    """
    x = np.linspace(rango_x[0], rango_x[1], 400)
    y = np.linspace(rango_y[0], rango_y[1], 400)
    X, Y = np.meshgrid(x, y)
    Z = np.array([[funcion(i, j) for i, j in zip(fila_x, fila_y)] for fila_x, fila_y in zip(X, Y)])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(titulo)
    plt.show()

funciones = {
    "Rastrigin": (rastrigin, [-5.12, 5.12], [-5.12, 5.12]),
    "Ackley": (ackley, [-5, 5], [-5, 5]),
    "Sphere": (sphere, [-5, 5], [-5, 5]),
    "Rosenbrock": (rosenbrock, [-2, 2], [-1, 3]),
    "Beale": (beale, [-4.5, 4.5], [-4.5, 4.5]),
    "Goldstein-Price": (goldstein_price, [-2, 2], [-2, 2]),
    "Booth": (booth, [-10, 10], [-10, 10]),
    "Bukin N.6": (bukin_n6, [-15, -5], [-3, 3]),
    "Matyas": (matyas, [-10, 10], [-10, 10]),
    "Levi N.13": (levi_n13, [-10, 10], [-10, 10]),
    "Himmelblau": (himmelblau, [-5, 5], [-5, 5]),
    "Camello Tres Jorobas": (camello_tres_jorobas, [-5, 5], [-5, 5]),
    "Easom": (easom, [-100, 100], [-100, 100]),
    "Cross-in-Tray": (cross_in_tray, [-10, 10], [-10, 10])
}

def graficar(funcion_nombre):
    """
    Grafica la función especificada por su nombre.

    Parámetros
    ----------
    funcion_nombre : str
        Nombre de la función a graficar.

    Retorna
    -------
    None
    """
    if funcion_nombre in funciones:
        funcion, rango_x, rango_y = funciones[funcion_nombre]
        graficar_funcion(funcion, rango_x, rango_y, funcion_nombre)
    else:
        print("Función no encontrada.")
