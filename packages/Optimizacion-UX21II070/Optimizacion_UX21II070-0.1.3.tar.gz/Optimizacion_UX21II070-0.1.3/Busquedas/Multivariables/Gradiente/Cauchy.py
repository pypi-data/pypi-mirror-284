"""
Módulo para optimización de funciones utilizando el método de Cauchy basado en el gradiente.

Este módulo contiene funciones para calcular el gradiente de una función y optimizarla
usando el método de Cauchy con varias estrategias de búsqueda unidireccional.

Funciones:
----------
- gradiante(f, x, deltaX=0.001):
    Calcula el gradiente de la función `f` en el punto `x`.

- cauchy(funcion, x0, epsilon1, epsilon2, M, Metodo_busqueda):
    Encuentra el punto mínimo óptimo de la función `funcion` utilizando el método de Cauchy basado en el gradiente.

- execute_total(funcion, x0, epsilon1, epsilon2, M, Metodo_busqueda):
    Ejecuta el proceso de optimización utilizando varios métodos de búsqueda unidireccional y muestra los resultados.

"""

import numpy as np


def cauchy(funcion, x0, epsilon1, epsilon2, M, Metodo_busqueda):
    """
    Encuentra el punto mínimo óptimo de la función `funcion` utilizando el método de Cauchy basado en el gradiente.

    Parámetros:
    -----------
    funcion : función
        La función objetivo que se quiere optimizar.
    x0 : array_like
        El punto inicial en el espacio de búsqueda.
    epsilon1 : float
        La tolerancia para el criterio de paro basado en el gradiente.
    epsilon2 : float
        La tolerancia para el criterio de paro de la búsqueda unidireccional.
    M : int
        El número máximo de iteraciones.
    Metodo_busqueda : función
        El método de búsqueda unidireccional a utilizar.

    Retorna:
    --------
    np.ndarray
        El punto óptimo encontrado.
    """
    terminar = False
    xk = x0
    k = 0
    while not terminar:
        grad = np.array(gradiante(funcion, xk))

        if np.linalg.norm(grad) < epsilon1 or k >= M:
            terminar = True
        else:
            def alpha_funcion(alpha):
                return funcion(xk - alpha * grad)
            
            alpha_resultado = Metodo_busqueda(alpha_funcion, epsilon=epsilon2, a=0.0, b=1.0)
            
            if isinstance(alpha_resultado, tuple):
                if len(alpha_resultado) == 2:
                    x_list = alpha_resultado[0]  # Primer lista de valores
                    if len(x_list) > 1:
                        # Toma el valor medio de la lista
                        alpha = (x_list[-2] + x_list[-1]) / 2
                    else:
                        # Si hay solo un valor, usa ese valor
                        alpha = x_list[0]
                else:
                    raise ValueError("El retorno del método de búsqueda no es válido: tupla con más de 2 elementos")
            elif isinstance(alpha_resultado, (list, np.ndarray)):
                if len(alpha_resultado) > 1:
                    alpha = (alpha_resultado[-2] + alpha_resultado[-1]) / 2
                else:
                    alpha = alpha_resultado[0]
            else:
                # Si alpha_resultado es un solo valor, úsalo directamente
                alpha = alpha_resultado
            
            alpha = Metodo_busqueda(alpha_funcion, epsilon=epsilon2, a=0.0, b=1.0)
            x_k1 = xk - alpha * grad

            if np.linalg.norm(x_k1 - xk) / (np.linalg.norm(xk) + 0.00001) <= epsilon2:
                terminar = True
            else:
                k += 1
                xk = x_k1
    return xk

def gradiante(f, x, deltaX=0.001):
    """
    Calcula el gradiente de la función `f` en el punto `x`.

    Parámetros:
    -----------
    f : función
        La función objetivo cuya gradiente se quiere calcular.
    x : array_like
        El punto en el que se quiere calcular el gradiente.
    deltaX : float, opcional
        El tamaño del paso para la aproximación numérica (por defecto es 0.001).

    Retorna:
    --------
    list
        El gradiente calculado en el punto `x`.
    """
    grad = []
    for i in range(len(x)):
        xp = x.copy()
        xn = x.copy()
        xp[i] += deltaX
        xn[i] -= deltaX
        grad.append((f(xp) - f(xn)) / (2 * deltaX))
    return grad



def execute_total(funcion, x0, epsilon1, epsilon2, M, Metodo_busqueda):
    """
    Ejecuta el proceso de optimización utilizando varios métodos de búsqueda unidireccional y muestra los resultados.

    Parámetros:
    -----------
    funcion : función
        La función objetivo que se quiere optimizar.
    x0 : array_like
        El punto inicial en el espacio de búsqueda.
    epsilon1 : float
        La tolerancia para el criterio de paro basado en el gradiente.
    epsilon2 : float
        La tolerancia para el criterio de paro de la búsqueda unidireccional.
    M : int
        El número máximo de iteraciones.
    Metodo_busqueda : función
        El método de búsqueda unidireccional a utilizar.

    Retorna:
    --------
    None
    """
    print("Resultado de búsqueda: ", cauchy(funcion, x0, epsilon1, epsilon2, M, Metodo_busqueda))
