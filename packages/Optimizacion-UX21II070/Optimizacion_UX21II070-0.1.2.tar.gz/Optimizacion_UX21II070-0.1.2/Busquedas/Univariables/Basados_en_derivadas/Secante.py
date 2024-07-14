"""
Módulo para cálculo de derivadas y búsqueda de raíces usando el método de la secante.

Este módulo contiene funciones para calcular la primera derivada de una función utilizando diferencias centrales,
y para encontrar puntos críticos de una función en un intervalo utilizando el método de la secante.

Funciones:
----------
- central_difference_first(f, x):
    Calcula la primera derivada de la función f en el punto x usando diferencias centrales.

- secante(fx, a, b, e):
    Encuentra puntos críticos de la función fx en el intervalo [a, b] utilizando el método de la secante.

- execute_total(fx, epsilon, lm, lM):
    Ejecuta el proceso de búsqueda de puntos críticos en el intervalo [lm, lM] y grafica la función fx.
"""

import numpy as np
import random
import matplotlib.pyplot as plt


def secante(fx, a, b, e):
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
    e : float
        La tolerancia para el criterio de parada.

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

    while xv1 == False or xv2 == False:
        
        if xv1 == False:
            r1 = central_difference_first(fx, x1) 
            if r1 < 0:
                xv1 = True
            else:
                x1 = random.uniform(a, b)
        if xv2 == False:
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

def central_difference_first(f, x):
    """
    Calcula la primera derivada de la función `f` en el punto `x` usando diferencias centrales.

    Parámetros:
    -----------
    f : función
        La función de la cual se quiere calcular la derivada.
    x : float
        El punto en el cual se quiere calcular la derivada.

    Retorna:
    --------
    float
        La derivada de `f` en el punto `x`.
    """
    if abs(x) > 0.01:
        delta = 0.01 * abs(x)
    else:
        delta = 0.0001
    return (f(x + delta) - f(x - delta)) / (2 * delta)


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

    x_p, y_p, z = secante(fx, lm, lM, epsilon)

    if len(x_p) == 0:
        plt.plot(x_vals, y_vals, label="No hay puntos críticos en este rango")
    else:
        print(x_p)
        print(y_p)
        print(z)

    plt.tight_layout()
    plt.show()
