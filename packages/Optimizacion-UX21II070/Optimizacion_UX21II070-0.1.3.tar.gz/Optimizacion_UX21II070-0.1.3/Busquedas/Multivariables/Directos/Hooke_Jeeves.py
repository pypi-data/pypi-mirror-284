import numpy as np

"""
Método de Optimización Hooke-Jeeves

El método Hooke-Jeeves es un algoritmo de optimización basado en una combinación de movimientos exploratorios y movimientos de búsqueda. Este método es particularmente útil para encontrar el mínimo de funciones no lineales y no diferenciables en espacios de búsqueda multidimensionales.

El algoritmo sigue dos fases principales:
1. **Movimiento Exploratorio**: Se exploran las direcciones en cada dimensión del espacio de búsqueda para encontrar una dirección en la que la función objetivo disminuya.
2. **Movimiento de Búsqueda**: Si el movimiento exploratorio encuentra una mejor solución, se realiza una búsqueda más profunda en esa dirección. Si no se encuentra una mejora, el tamaño del paso se reduce y se repite el proceso.

El algoritmo termina cuando el tamaño del paso es menor que un umbral predefinido (`epsilon`).

El método incluye las siguientes funciones:
- `hooke_jeeves`: Implementa el algoritmo Hooke-Jeeves para la optimización.
- `exploratory_move`: Realiza un movimiento exploratorio en el espacio de búsqueda.
- `execute_total`: Ejecuta el proceso de optimización y muestra los resultados.
"""


def hooke_jeeves(fx, p, delta, alpha=2, epsilon=1e-6):
    """
    Encuentra el punto mínimo óptimo de la función `fx` utilizando el método Hooke-Jeeves.

    Parámetros:
    -----------
    fx : función
        La función objetivo que se quiere optimizar.
    p : array_like
        El punto inicial en el espacio de búsqueda.
    delta : array_like
        El tamaño del paso en cada dirección.
    alpha : float, opcional
        El factor de reducción del tamaño del paso (por defecto es 2).
    epsilon : float, opcional
        La tolerancia para el criterio de parada (por defecto es 1e-6).

    Retorna:
    --------
    tuple
        El punto óptimo encontrado y la lista de puntos visitados.

    Funciones internas:
    -------------------
    - `exploratory_move(fx, xc, d, puntos)`: Realiza un movimiento exploratorio en el espacio de búsqueda.
    - `execute_total(fx, p, delta)`: Ejecuta el proceso de optimización y muestra los resultados.
    """
    k = 0
    xp = [0, 0]
    xk = [0, 0]
    step = 2
    xk[k] = p

    puntos = []

    puntos.append(p)

    while np.linalg.norm(delta) > epsilon:
        if step == 2:
            r_e, puntos = exploratory_move(fx, xk[k], delta, puntos)
            xk[k+1] = r_e

            if np.all(r_e == -1):
                step = 3
            else:
                step = 4

        if step == 3:
            norma = np.linalg.norm(delta)
            if norma < epsilon:
                return xk[k], puntos
            else:
                for i in range(len(delta)):
                    delta[i] /= alpha 
            step = 2           

        if step == 4:
            k = k + 1
            xp.append(0)
            puntos.append(xp[k])
            x_p = xk[k] + (xk[k] - xk[k-1])
            xp[k+1] = x_p

            step = 5

        if step == 5:
            r_e, puntos = exploratory_move(fx, xp[k+1], delta, puntos)
            xk.append(0)
            puntos.append(xk[k])
            xk[k+1] = r_e
            if np.all(r_e == -1):
                step = 3
            else:
                step = 6
        
        if step == 6:
            if fx(xk[k+1]) < fx(xk[k]):
                step = 4
            else:
                step = 3

    puntos =  [x for x in puntos if isinstance(x, np.ndarray)]   

    return xk[k], puntos

def exploratory_move(fx, xc, d, puntos):
    """
    Realiza un movimiento exploratorio en el espacio de búsqueda.

    Parámetros:
    -----------
    fx : función
        La función objetivo que se quiere optimizar.
    xc : array_like
        El punto actual en el espacio de búsqueda.
    d : array_like
        El tamaño del paso en cada dirección.
    puntos : list
        Lista de puntos visitados durante la exploración.

    Retorna:
    --------
    tuple
        El nuevo punto encontrado y la lista de puntos visitados.
    """
    n = len(xc)
    i = 0
    x = xc.copy()
    
    while i < n:
        x_plus = x.copy()
        x_down = x.copy()

        x_plus[i] += d[i]
        x_down[i] -= d[i]

        puntos.append(x_plus)
        puntos.append(x_down)

        v_positivo = fx(x_plus)
        v = fx(xc)
        v_negativo = fx(x_down)

        fmin = min(v, v_positivo, v_negativo)

        if fmin == v_positivo:
            x = x_plus
        elif fmin == v_negativo:
            x = x_down
        i += 1

    if not np.all(x == xc):
        return x, puntos
    else:
        return -1, puntos



def execute_total(fx, p, delta):
    """
    Ejecuta el proceso de optimización y muestra los resultados.

    Parámetros:
    -----------
    fx : función
        La función objetivo que se quiere optimizar.
    p : array_like
        El punto inicial en el espacio de búsqueda.
    delta : array_like
        El tamaño del paso en cada dirección.

    Retorna:
    --------
    None
    """
    v_found, points = hooke_jeeves(fx, p, delta, alpha=2, epsilon=1e-6)
    print(f"El punto óptimo encontrado es: {v_found} donde el valor al evaluarlo es {fx(v_found)}")
    print("Puntos que visitó Hooke-Jeeves: ", points)
