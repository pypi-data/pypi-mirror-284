"""
Módulo para cálculo de derivadas y búsqueda de puntos mínimos óptimos usando el método de Newton-Raphson.

Este módulo contiene funciones para calcular la primera y segunda derivada de una función utilizando diferencias centrales,
y para encontrar puntos críticos de una función en un intervalo utilizando el método de Newton-Raphson.

Funciones:
----------
- central_difference_first(f, x, delta=0.0001):
    Calcula la primera derivada de la función f en el punto x usando diferencias centrales.

- central_difference_second(f, x, delta=0.0001):
    Calcula la segunda derivada de la función f en el punto x usando diferencias centrales.

- newton_raphson(f, lm, epsilon=1e-8, max_iterations=100):
    Encuentra puntos críticos de la función f comenzando en el punto lm utilizando el método de Newton-Raphson.

- execute_total(fx, epsilon=1e-8, lm=-10, lM=10):
    Ejecuta el proceso de búsqueda de puntos críticos en el intervalo [lm, lM] y grafica la función fx.
"""

import numpy as np
import matplotlib.pyplot as plt


def newton_raphson(f, lm, epsilon=1e-8, max_iterations=100):
    """
    Encuentra puntos críticos de la función `f` comenzando en el punto `lm` utilizando el método de Newton-Raphson.

    Parámetros:
    -----------
    f : función
        La función de la cual se quieren encontrar los puntos críticos.
    lm : float
        El punto inicial para el método de Newton-Raphson.
    epsilon : float, opcional
        La tolerancia para el criterio de parada. El valor predeterminado es 1e-8.
    max_iterations : int, opcional
        El número máximo de iteraciones permitidas. El valor predeterminado es 100.

    Retorna:
    --------
    tuple
        Una tupla que contiene el punto crítico encontrado `x_next` y una lista de valores `x_values` durante las iteraciones.
    """
    x = lm
    k = 1
    x_values = []
    
    f_prime = central_difference_first(f, x)

    while abs(f_prime) > epsilon and k < max_iterations:
        f_prime = central_difference_first(f, x)
        f_double_prime = central_difference_second(f, x)
        
        if f_double_prime == 0:
            return -1, x_values  # Evita división por cero
        
        x_next = x - f_prime / f_double_prime
        
        x_values.append(x)
        x = x_next
        k += 1
        
        f_prime = central_difference_first(f, x)

    return x_next, x_values


def central_difference_first(f, x, delta=0.0001):
    """
    Calcula la primera derivada de la función `f` en el punto `x` usando diferencias centrales.

    Parámetros:
    -----------
    f : función
        La función de la cual se quiere calcular la derivada.
    x : float
        El punto en el cual se quiere calcular la derivada.
    delta : float, opcional
        El tamaño del paso para las diferencias centrales. El valor predeterminado es 0.0001.

    Retorna:
    --------
    float
        La derivada de `f` en el punto `x`.
    """
    if abs(x) > 0.01:
        delta = 0.01 * abs(x)
    return (f(x + delta) - f(x - delta)) / (2 * delta)


def central_difference_second(f, x, delta=0.0001):
    """
    Calcula la segunda derivada de la función `f` en el punto `x` usando diferencias centrales.

    Parámetros:
    -----------
    f : función
        La función de la cual se quiere calcular la derivada.
    x : float
        El punto en el cual se quiere calcular la derivada.
    delta : float, opcional
        El tamaño del paso para las diferencias centrales. El valor predeterminado es 0.0001.

    Retorna:
    --------
    float
        La segunda derivada de `f` en el punto `x`.
    """
    if abs(x) > 0.01:
        delta = 0.01 * abs(x)
    return (f(x + delta) - 2*f(x) + f(x - delta)) / (delta**2)


def execute_total(fx, epsilon=1e-8, lm=-10, lM=10):
    """
    Ejecuta el proceso de búsqueda de puntos críticos en el intervalo `[lm, lM]` y grafica la función `fx`.

    Parámetros:
    -----------
    fx : función
        La función de la cual se quieren encontrar los puntos críticos y graficar.
    epsilon : float, opcional
        La tolerancia para el criterio de parada. El valor predeterminado es 1e-8.
    lm : float, opcional
        El límite inferior del intervalo. El valor predeterminado es -10.
    lM : float, opcional
        El límite superior del intervalo. El valor predeterminado es 10.
    """
    x_vals = np.linspace(lm, lM, 100)
    y_vals = fx(x_vals)

    x, x_valores = newton_raphson(fx, lm, epsilon)

    if x == -1:
        plt.plot(x_vals, y_vals, label="No hay puntos críticos en este rango")
    else:
        plt.plot(x_vals, y_vals)
        plt.scatter(x_valores, [fx(x) for x in x_valores], color='red')

        legend_text = "\n".join([f'{i+1}: ({x:.2f}, {fx(x):.2f})' for i, x in enumerate(x_valores)])
        plt.legend([legend_text], loc='upper right')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    plt.tight_layout()
    plt.show()
