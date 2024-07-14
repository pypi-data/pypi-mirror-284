"""
Módulo de funciones de optimización y visualización
===================================================

Este módulo contiene varias funciones matemáticas utilizadas en optimización,
así como métodos para graficar estas funciones en 3D, incluyendo posibles restricciones.

Funciones
---------
- `rosenbrock(x, y=1)`: Función de Rosenbrock.
- `pajaro_mishra(x, y=1)`: Función de Pájaro-Mishra.
- `townsend(x, y=1)`: Función de Townsend.
- `gomez_levy(x, y=1)`: Función de Gomez-Levy.
- `simionescu(x, y=1)`: Función de Simionescu.

Métodos
-------
- `graficar_funcion(funcion, rango_x, rango_y, nombre_funcion, tipo_restriccion=None)`: Método para graficar funciones en 3D.
- `graficar(nombre_funcion)`: Método para seleccionar y graficar una función predefinida.
"""

import numpy as np
import matplotlib.pyplot as plt

def rosenbrock(x, y=1):
    """
    Función de Rosenbrock.

    Parámetros
    ----------
    x : float
        Valor de entrada para la dimensión x.
    y : float, opcional
        Valor de entrada para la dimensión y (por defecto es 1).

    Retorna
    -------
    float
        Valor de salida de la función de Rosenbrock.
    """
    return (1 - x)**2 + 100 * (y - x**2)**2

def pajaro_mishra(x, y=1):
    """
    Función de Pájaro-Mishra.

    Parámetros
    ----------
    x : float
        Valor de entrada para la dimensión x.
    y : float, opcional
        Valor de entrada para la dimensión y (por defecto es 1).

    Retorna
    -------
    float
        Valor de salida de la función de Pájaro-Mishra.
    """
    return np.sin(y) * np.exp((1 - np.cos(x))**2) + np.cos(x) * np.exp((1 - np.sin(y))**2) + (x - y)**2

def townsend(x, y=1):
    """
    Función de Townsend.

    Parámetros
    ----------
    x : float
        Valor de entrada para la dimensión x.
    y : float, opcional
        Valor de entrada para la dimensión y (por defecto es 1).

    Retorna
    -------
    float
        Valor de salida de la función de Townsend.
    """
    return np.log(np.abs(x**2 + y**2 - 1) + 0.1) + (x - y)**2

def gomez_levy(x, y=1):
    """
    Función de Gomez-Levy.

    Parámetros
    ----------
    x : float
        Valor de entrada para la dimensión x.
    y : float, opcional
        Valor de entrada para la dimensión y (por defecto es 1).

    Retorna
    -------
    float
        Valor de salida de la función de Gomez-Levy.
    """
    return np.sin(x)**10 + np.cos(y)**10

def simionescu(x, y=1):
    """
    Función de Simionescu.

    Parámetros
    ----------
    x : float
        Valor de entrada para la dimensión x.
    y : float, opcional
        Valor de entrada para la dimensión y (por defecto es 1).

    Retorna
    -------
    float
        Valor de salida de la función de Simionescu.
    """
    return 0.1 * x * y


funciones = {
    "Rosenbrock_CubicLine": (rosenbrock, [-2, 2], [-1, 3], "cúbica_linea"),
    "Rosenbrock_Disk": (rosenbrock, [-2, 2], [-2, 2], "disco"),
    "Pajaro_Mishra": (pajaro_mishra, [-10, 0], [-10, 0], "circulo"),
    "Townsend": (townsend, [-2, 2], [-2, 2], None),
    "Gomez_Levy": (gomez_levy, [-2 * np.pi, 2 * np.pi], [-2 * np.pi, 2 * np.pi], None),
    "Simionescu": (simionescu, [-1.5, 1.5], [-1.5, 1.5], "simionescu")
}

def graficar_funcion(funcion, rango_x, rango_y, nombre_funcion, tipo_restriccion=None):
    """
    Grafica una función en 3D, aplicando restricciones específicas si es necesario.

    Parámetros
    ----------
    funcion : callable
        La función a graficar.
    rango_x : list[float, float]
        El rango de valores para la dimensión x.
    rango_y : list[float, float]
        El rango de valores para la dimensión y.
    nombre_funcion : str
        Nombre de la función para el título del gráfico.
    tipo_restriccion : str, opcional
        Tipo de restricción a aplicar (por defecto es None).

    Retorna
    -------
    None
    """
    x = np.linspace(rango_x[0], rango_x[1], 400)
    y = np.linspace(rango_y[0], rango_y[1], 400)
    X, Y = np.meshgrid(x, y)
    Z = funcion(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.7)

    # Aplicar restricciones específicas
    if tipo_restriccion == "cúbica_linea":
        restriccion_x = np.linspace(-1.5, 1.5, 400)
        restriccion_y = restriccion_x**3 - restriccion_x
        restriccion_z = funcion(restriccion_x, restriccion_y)
        ax.plot(restriccion_x, restriccion_y, restriccion_z, 'r-', label='$y = x^3 - x$')
    
    elif tipo_restriccion == "disco":
        theta = np.linspace(0, 2 * np.pi, 400)
        disco_x = np.sqrt(2) * np.cos(theta)
        disco_y = np.sqrt(2) * np.sin(theta)
        disco_z = funcion(disco_x, disco_y)
        ax.plot(disco_x, disco_y, disco_z, 'r-', label='$x^2 + y^2 = 2$')
    
    elif tipo_restriccion == "circulo":
        theta = np.linspace(0, 2 * np.pi, 400)
        circulo_x = -5 + 5 * np.cos(theta)
        circulo_y = -5 + 5 * np.sin(theta)
        circulo_z = funcion(circulo_x, circulo_y)
        ax.plot(circulo_x, circulo_y, circulo_z, 'r-', label='$(x+5)^2 + (y+5)^2 = 25$')
    
    elif tipo_restriccion == "simionescu":
        theta = np.linspace(0, 2 * np.pi, 400)
        R = 1 + 0.2 * np.cos(8 * theta)
        x_frontera = R * np.cos(theta)
        y_frontera = R * np.sin(theta)
        ax.plot(x_frontera, y_frontera, funcion(x_frontera, y_frontera), 'r-', label='Límite de restricción')

    plt.legend()
    ax.set_title(nombre_funcion)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('f(x, y)')
    plt.show()

def graficar(nombre_funcion):
    """
    Grafica la función especificada por su nombre.

    Parámetros
    ----------
    nombre_funcion : str
        Nombre de la función a graficar.

    Retorna
    -------
    None
    """
    if nombre_funcion in funciones:
        funcion, rango_x, rango_y, tipo_restriccion = funciones[nombre_funcion]
        graficar_funcion(funcion, rango_x, rango_y, nombre_funcion, tipo_restriccion)
    else:
        print("Función no encontrada.")
