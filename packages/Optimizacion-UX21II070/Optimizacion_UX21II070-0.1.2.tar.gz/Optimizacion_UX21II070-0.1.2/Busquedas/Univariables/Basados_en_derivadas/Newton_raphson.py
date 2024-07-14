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

- newton_raphson(f, lm, epsilon, max_iterations=100):
    Encuentra puntos críticos de la función f comenzando en el punto lm utilizando el método de Newton-Raphson.

- execute_total(fx, epsilon, lm, lM):
    Ejecuta el proceso de búsqueda de puntos críticos en el intervalo [lm, lM] y grafica la función fx.
"""

import numpy as np
import matplotlib.pyplot as plt


def newton_raphson(f, lm, epsilon, max_iterations=100):
    """
    Encuentra puntos críticos de la función `f` comenzando en el punto `lm` utilizando el método de Newton-Raphson.

    Parámetros:
    -----------
    f : función
        La función de la cual se quieren encontrar los puntos críticos.
    lm : float
        El punto inicial para el método de Newton-Raphson.
    epsilon : float
        La tolerancia para el criterio de parada.
    max_iterations : int, opcional
        El número máximo de iteraciones permitidas (por defecto es 100).

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
        x_next = x - f_prime / f_double_prime
        
        if abs(f_prime) < epsilon:
            return x_next, x_values 
        
        x = x_next
        x_values.append(x)
        k += 1

        if k == max_iterations: 
            return -1, 0

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
        El tamaño del paso para las diferencias centrales (por defecto es 0.0001).

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
        El tamaño del paso para las diferencias centrales (por defecto es 0.0001).

    Retorna:
    --------
    float
        La segunda derivada de `f` en el punto `x`.
    """
    if abs(x) > 0.01:
        delta = 0.01 * abs(x)
    return (f(x + delta) - 2*f(x) + f(x - delta)) / (delta**2)



def execute_total(fx, epsilon, lm, lM):
    """
    Ejecuta el proceso de búsqueda de puntos críticos en el intervalo `[lm, lM]` y grafica la función `fx`.

    Parámetros:
    -----------
    fx : función
        La función de la cual se quieren encontrar los puntos críticos y graficar.
    epsilon : float
        La tolerancia para el criterio de parada.
    lm : float
        El límite inferior del intervalo.
    lM : float
        El límite superior del intervalo.
    """
    x_vals = np.linspace(lm, lM, 100)
    y_vals = fx(x_vals)

    x, x_valores = newton_raphson(fx, lm, epsilon)

    if x == -1:
        plt.plot(x_vals, y_vals, label="No hay puntos críticos en este rango")
        plt.legend()

    else:
        plt.plot(x_vals, y_vals)
        plt.scatter(x_valores, [fx(x) for x in x_valores], color='red')

        for i, (x, y) in enumerate(zip(x_valores, [fx(root) for root in x_valores])):
            legend_text = "\n".join([f'{i+1}: ({x:.2f}, {fx(x):.2f})' for i, x in enumerate(x_valores)])
        plt.legend([legend_text], loc='upper right')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    plt.tight_layout()
    plt.show()
