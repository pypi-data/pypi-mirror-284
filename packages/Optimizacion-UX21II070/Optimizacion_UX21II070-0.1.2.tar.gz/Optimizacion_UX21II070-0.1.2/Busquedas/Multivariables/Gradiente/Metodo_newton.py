"""
Módulo para optimización de funciones utilizando el método de Newton.

Este módulo contiene funciones para calcular el gradiente y la matriz Hessiana de una función,
y optimizarla usando el método de Newton con varias estrategias de búsqueda unidireccional.

Funciones:
----------
- gradiante(f, x, deltaX=0.001):
    Calcula el gradiente de la función `f` en el punto `x`.

- hessian_matrix(f, x, deltax):
    Calcula la matriz Hessiana de la función `f` en el punto `x`.

- Newton(funcion, x0, epsilon1, epsilon2, M, Metodo_busqueda):
    Encuentra el punto mínimo óptimo de la función `funcion` utilizando el método de Newton.

- execute_total(funcion, x0, epsilon1, epsilon2, M, Metodo_busqueda):
    Ejecuta el proceso de optimización utilizando el método de Newton y muestra los resultados.

"""

import numpy as np

def Newton(funcion, x0, epsilon1, epsilon2, M, Metodo_busqueda):
    """
    Encuentra el punto mínimo óptimo de la función `funcion` utilizando el método de Newton.

    Parámetros:
    -----------
    funcion : función
        La función objetivo que se quiere optimizar.
    x0 : array_like
        El punto inicial en el espacio de búsqueda.
    epsilon1 : float
        La tolerancia para el criterio de paro basado en el gradiente.
    epsilon2 : float
        La tolerancia para el criterio de paro basado en el cambio relativo del punto.
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
        hessian = hessian_matrix(funcion, xk, 1)
        hessian_inv = np.linalg.inv(hessian)
        grad = np.array(gradiante(funcion, xk))

        if np.linalg.norm(grad) < epsilon1 or k >= M:
            terminar = True
        else:
            def alpha_funcion(alpha):
                return funcion(xk - alpha * (np.dot(hessian_inv, grad)))
            
            alpha = Metodo_busqueda(alpha_funcion, epsilon=epsilon2, a=0.0, b=1.0)

            v = np.dot(grad.T, np.dot(hessian_inv, grad))
            if v > 0:
                x_k1 = xk - alpha * (np.dot(hessian_inv, grad))

                if np.linalg.norm(x_k1 - xk) / (np.linalg.norm(xk) + 0.00001) <= epsilon2:
                    terminar = True
                else:
                    k += 1
                    xk = x_k1
            else:
                xk = np.random.uniform(-5.0, 5.0, size=2)
                k = 0
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
        xp[i] = xp[i] + deltaX
        xn[i] = xn[i] - deltaX
        grad.append((f(xp) - f(xn)) / (2 * deltaX))
    return grad

def hessian_matrix(f, x, deltax):
    """
    Calcula la matriz Hessiana de la función `f` en el punto `x`.

    Parámetros:
    -----------
    f : función
        La función objetivo cuya matriz Hessiana se quiere calcular.
    x : array_like
        El punto en el que se quiere calcular la matriz Hessiana.
    deltax : float
        El tamaño del paso para la aproximación numérica.

    Retorna:
    --------
    list
        La matriz Hessiana calculada en el punto `x`.
    """
    fx = f(x)
    n = len(x)
    H = []
    for i in range(n):
        hi = []
        for j in range(n):
            if i == j:
                xp = x.copy()
                xn = x.copy()
                xp[i] = xp[i] + deltax
                xn[i] = xn[i] - deltax
                hi.append((f(xp) - 2 * fx + f(xn)) / (deltax**2))
            else:
                xpp = x.copy()
                xpn = x.copy()
                xnp = x.copy()
                xnn = x.copy()
                
                xpp[i] = xpp[i] + deltax
                xpp[j] = xpp[j] + deltax

                xpn[i] = xpn[i] + deltax
                xpn[j] = xpn[j] - deltax
                
                xnp[i] = xnp[i] - deltax
                xnp[j] = xnp[j] + deltax

                xnn[i] = xnn[i] - deltax
                xnn[j] = xnn[j] - deltax

                hi.append((f(xpp) - f(xpn) - f(xnp) + f(xnn)) / (4 * (deltax**2)))
        H.append(hi)
    return H


def execute_total(funcion, x0, epsilon1, epsilon2, M, Metodo_busqueda):
    """
    Ejecuta el proceso de optimización utilizando el método de Newton y muestra los resultados.

    Parámetros:
    -----------
    funcion : función
        La función objetivo que se quiere optimizar.
    x0 : array_like
        El punto inicial en el espacio de búsqueda.
    epsilon1 : float
        La tolerancia para el criterio de paro basado en el gradiente.
    epsilon2 : float
        La tolerancia para el criterio de paro basado en el cambio relativo del punto.
    M : int
        El número máximo de iteraciones.
    Metodo_busqueda : función
        El método de búsqueda unidireccional a utilizar.

    Retorna:
    --------
    None
    """
    resultado = Newton(funcion, x0, epsilon1, epsilon2, M, Metodo_busqueda)
    print(f"Resultado de búsqueda: {resultado}")
