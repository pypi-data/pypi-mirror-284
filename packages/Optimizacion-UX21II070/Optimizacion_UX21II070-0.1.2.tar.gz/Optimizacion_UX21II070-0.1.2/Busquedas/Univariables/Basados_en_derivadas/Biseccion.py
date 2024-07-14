"""
Módulo para cálculo de derivadas y búsqueda de puntos mínimos óptimos usando el método de la bisección.

Este módulo contiene funciones para calcular la primera derivada de una función utilizando diferencias centrales,
y para encontrar puntos críticos de una función en un intervalo utilizando el método de la bisección.

Funciones:
----------
- central_difference_first(f, x):
    Calcula la primera derivada de la función f en el punto x usando diferencias centrales.

- Biseccion(fx, a, b, e):
    Encuentra puntos críticos de la función fx en el intervalo [a, b] utilizando el método de la bisección.

- execute_total(fx, epsilon, lm, lM):
    Ejecuta el proceso de búsqueda de puntos críticos en el intervalo [lm, lM] y grafica la función fx.
"""

import numpy as np
import random
import matplotlib.pyplot as plt

def Biseccion(fx, a, b, e):
    """
    Encuentra puntos críticos de la función `fx` en el intervalo `[a, b]` utilizando el método de la bisección.

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

    x1 = random.uniform(a, b)
    x2 = random.uniform(a, b)

    xv1 = False
    xv2 = False
    z = 0

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
        if n > 1000:
            return z
        
        if xv1 and xv2:
            while True:
                z = (x2 + x1) / 2
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

    x_p, y_p, z = Biseccion(fx, lm, lM, epsilon)
    
    if len(x_p) == 0:
        plt.plot(x_vals, y_vals, label="No hay puntos críticos en este rango")
    else:
        plt.plot(x_vals, y_vals)
        for i, (x, y) in enumerate(zip(x_p, y_p)):
            plt.scatter(x, y, label=f'Punto {i+1}: ({x:.2f}, {y:.2f})')
        plt.scatter(z, fx(z), label=f"valor z_final: ({z:.2f}, {fx(z):.2f})")
    
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()
