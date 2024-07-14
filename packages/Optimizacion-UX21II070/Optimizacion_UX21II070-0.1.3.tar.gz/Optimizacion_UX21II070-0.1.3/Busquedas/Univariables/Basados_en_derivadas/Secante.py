"""
Módulo para cálculo de derivadas y búsqueda de raíces usando el método de la secante.

Este módulo contiene funciones para calcular la primera derivada de una función utilizando diferencias centrales,
y para encontrar puntos críticos de una función en un intervalo utilizando el método de la secante.

Funciones:
----------
- central_difference_first(f, x, delta=0.0001):
    Calcula la primera derivada de la función f en el punto x usando diferencias centrales.

- secante(fx, a, b, e=0.00001):
    Encuentra puntos críticos de la función fx en el intervalo [a, b] utilizando el método de la secante.

- execute_total(fx, epsilon=0.00001, lm=-10, lM=10):
    Ejecuta el proceso de búsqueda de puntos críticos en el intervalo [lm, lM] y grafica la función fx.
"""

import numpy as np
import random
import matplotlib.pyplot as plt


def secante(fx, a, b, e=0.00001):
    """
    Encuentra puntos críticos de la función `fx` en el intervalo `[a, b]` utilizando el método de la secante.

    Parámetros:
    -----------
    fx : función
        La función de la cual se quieren encontrar los puntos críticos.
    a : float
        El límite inferior del intervalo.
    b : float
        El límite superior del intervalo.
    e : float, opcional
        La tolerancia para el criterio de parada. El valor predeterminado es 0.00001.

    Retorna:
    --------
    tuple
        Una tupla que contiene una lista de valores `x`, una lista de valores `y` correspondientes y 
        el punto crítico encontrado `z`.
    """
    x_values = []
    y_values = []
    z = 0

    x1 = random.uniform(a, b)
    x2 = random.uniform(a, b)

    xv1 = False
    xv2 = False
    
    n = 0

    while not xv1 or not xv2:
        
        if not xv1:
            r1 = central_difference_first(fx, x1) 
            if r1 < 0:
                xv1 = True
            else:
                x1 = random.uniform(a, b)
        if not xv2:
            r2 = central_difference_first(fx, x2) 
            if r2 > 0:
                xv2 = True
            else:
                x2 = random.uniform(a, b)  

        n += 1
        if n > 100:
            return x_values, y_values, z
        
        if xv1 and xv2:
            while True:
                f_prime_x1 = central_difference_first(fx, x1)
                f_prime_x2 = central_difference_first(fx, x2)
                if f_prime_x2 == f_prime_x1:
                    return x_values, y_values, z  # Evita división por cero
                
                z = x2 - (central_difference_first(fx, x2) / 
                          ((central_difference_first(fx, x2) - central_difference_first(fx, x1)) / (x2 - x1)))
                derivative_z = central_difference_first(fx, z)

                if x2 > b or x1 < a:
                    return x_values, y_values, z

                if abs(derivative_z) <= e:
                    x_values = [x1, x2]
                    y_values = [fx(x1), fx(x2)]
                    return x_values, y_values, z
                elif derivative_z < 0:
                    x1 = z
                else:
                    x2 = z


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


def execute_total(fx, epsilon=0.00001, lm=-10, lM=10):
    """
    Ejecuta el proceso de búsqueda de puntos críticos en el intervalo `[lm, lM]` y grafica la función `fx`.

    Parámetros:
    -----------
    fx : función
        La función de la cual se quieren encontrar los puntos críticos y graficar.
    epsilon : float, opcional
        La tolerancia para el criterio de parada. El valor predeterminado es 0.00001.
    lm : float, opcional
        El límite inferior del intervalo. El valor predeterminado es -10.
    lM : float, opcional
        El límite superior del intervalo. El valor predeterminado es 10.
    """
    x_vals = np.linspace(lm, lM, 100)
    y_vals = fx(x_vals)

    x_p, y_p, z = secante(fx, lm, lM, epsilon)

    if len(x_p) == 0:
        plt.plot(x_vals, y_vals, label="No hay puntos críticos en este rango")
    else:
        plt.plot(x_vals, y_vals)
        plt.scatter(x_p, y_p, color='red')

        legend_text = "\n".join([f'{i+1}: ({x:.2f}, {fx(x):.2f})' for i, x in enumerate(x_p)])
        plt.legend([legend_text], loc='upper right')
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    plt.tight_layout()
    plt.show()
