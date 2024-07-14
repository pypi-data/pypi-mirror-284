"""
Módulo para optimización de funciones utilizando el método del gradiente conjugado.

Este módulo contiene funciones para calcular el gradiente de una función y optimizarla
usando el método del gradiente conjugado con varias estrategias de búsqueda unidireccional.

Funciones:
----------
- gradiante(f, x, deltaX=0.001):
    Calcula el gradiente de la función `f` en el punto `x`.

- gradiante_conjugado(funcion, x0, epsilon1, epsilon2, epsilon3, M, Metodo_busqueda):
    Encuentra el punto mínimo óptimo de la función `funcion` utilizando el método del gradiente conjugado.

- execute_total(funcion, x0, epsilon1, epsilon2, epsilon3, iteraciones, Metodo_busqueda):
    Ejecuta el proceso de optimización utilizando el método del gradiente conjugado y muestra los resultados.

"""

import numpy as np

def gradiante_conjugado(funcion, x0, epsilon1, epsilon2, epsilon3, M, Metodo_busqueda):
    """
    Encuentra el punto mínimo óptimo de la función `funcion` utilizando el método del gradiente conjugado.

    Parámetros:
    -----------
    funcion : función
        La función objetivo que se quiere optimizar.
    x0 : array_like
        El punto inicial en el espacio de búsqueda.
    epsilon1 : float
        La tolerancia para el criterio de paro basado en el tamaño del paso.
    epsilon2 : float
        La tolerancia para el criterio de paro basado en la búsqueda unidireccional.
    epsilon3 : float
        La tolerancia para el criterio de paro basado en la norma del punto.
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
    grad = np.array(gradiante(funcion, xk)) * -1
    while not terminar:
        if k >= M:
            terminar = True
        else:
            def alpha_funcion(alpha):
                return funcion(xk + alpha * grad)
            
            alpha = Metodo_busqueda(alpha_funcion, epsilon=epsilon2, a=0.0, b=1.0)

            if alpha < epsilon1:
                return xk
            
            x_k1 = xk + alpha * grad

            grad = (np.array(gradiante(funcion, x_k1)) * -1) + \
                   (np.linalg.norm(np.array(gradiante(funcion, x_k1))) ** 2 / np.linalg.norm(grad) ** 2) * grad

            if Metodo_busqueda(alpha_funcion, epsilon=epsilon2, a=0.0, b=1.0) < epsilon1:
                terminar = True

            if np.linalg.norm(x_k1 - xk) / (np.linalg.norm(xk) + 0.00001) <= epsilon2 or np.linalg.norm(x_k1) <= epsilon3:
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



def execute_total(funcion, x0, epsilon1, epsilon2, epsilon3, iteraciones, Metodo_busqueda):
    """
    Ejecuta el proceso de optimización utilizando el método del gradiente conjugado y muestra los resultados.

    Parámetros:
    -----------
    funcion : función
        La función objetivo que se quiere optimizar.
    x0 : array_like
        El punto inicial en el espacio de búsqueda.
    epsilon1 : float
        La tolerancia para el criterio de paro basado en el tamaño del paso.
    epsilon2 : float
        La tolerancia para el criterio de paro basado en la búsqueda unidireccional.
    epsilon3 : float
        La tolerancia para el criterio de paro basado en la norma del punto.
    iteraciones : int
        El número máximo de iteraciones.
    Metodo_busqueda : función
        El método de búsqueda unidireccional a utilizar.

    Retorna:
    --------
    None
    """
    print("Resultado de búsqueda: ", gradiante_conjugado(funcion, x0, epsilon1, epsilon2, epsilon3, iteraciones, Metodo_busqueda))
