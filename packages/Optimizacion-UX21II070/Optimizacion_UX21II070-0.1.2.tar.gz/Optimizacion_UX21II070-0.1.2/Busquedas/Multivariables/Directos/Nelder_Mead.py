import numpy as np

"""
Método de Optimización Nelder-Mead Simplex

El método Nelder-Mead Simplex es un algoritmo de optimización basado en la construcción de un simplex en el espacio de búsqueda para encontrar el mínimo de una función objetivo. Este método es útil para problemas de optimización sin requerimientos de derivadas y se aplica comúnmente a funciones no lineales.

El algoritmo se basa en la evolución de un conjunto de puntos (simplex) para explorar el espacio de búsqueda. A lo largo del proceso, el algoritmo realiza tres operaciones principales:
1. **Reflexión**: Se calcula un nuevo punto reflejado con respecto al centroide del simplex.
2. **Expansión**: Si el nuevo punto reflejado mejora la solución, se expande el simplex en esa dirección.
3. **Contracción**: Si el punto reflejado no mejora la solución, el algoritmo contrae el simplex.

El algoritmo termina cuando el cambio en los valores de la función objetivo entre iteraciones es menor que un umbral predefinido (`epsilon`).

El método incluye las siguientes funciones:
- `Nelder_mead_simplex`: Implementa el algoritmo Nelder-Mead para la optimización.
- `generar_simplex1`: Genera el simplex inicial para el método Nelder-Mead.
- `execute_total`: Ejecuta el proceso de optimización y muestra los resultados.
"""

def Nelder_mead_simplex(funcion_objetivo, p, gamma=2, beta=0.5, epsilon=1e-3):
    """
    Encuentra el punto mínimo óptimo de la función `funcion_objetivo` utilizando el método Nelder-Mead.

    Parámetros:
    -----------
    funcion_objetivo : función
        La función objetivo que se quiere optimizar.
    p : array_like
        El punto inicial en el espacio de búsqueda.
    gamma : float, opcional
        El factor de expansión (por defecto es 2).
    beta : float, opcional
        El factor de contracción (por defecto es 0.5).
    epsilon : float, opcional
        La tolerancia para el criterio de parada (por defecto es 1e-3).

    Retorna:
    --------
    np.ndarray
        El punto óptimo encontrado.
    """
    n = len(p)
    simplex = generar_simplex1(p)
    valores = [funcion_objetivo(point) for point in simplex]
    xl_index = np.argmin(valores)
    xh_index = np.argmax(valores)
    xg_index = None
    for i in range(len(valores)):
        if valores[i] < valores[xh_index]:
            xg_index = i
    
    if xg_index is None:
        xg_index = xl_index
   
    xc = np.mean(np.delete(simplex, xh_index, axis=0), axis=0)

    iteraciones = 0

    while (np.sqrt(np.sum((valores - funcion_objetivo(xc))**2 / (n + 1))) >= epsilon and iteraciones < 100):
        iteraciones += 1 
        valores = [funcion_objetivo(point) for point in simplex]
        xl_index = np.argmin(valores)
        xh_index = np.argmax(valores)
        
        for i in range(len(valores)):
            if valores[i] < valores[xh_index]:
                xg_index = i

        if xg_index is None:
            xg_index = xl_index        

        xc = np.mean(np.delete(simplex, xh_index, axis=0), axis=0)
        
        xr = 2 * xc - simplex[xh_index]
        x_new = xr
        fxr = funcion_objetivo(xr)
        
        if fxr < valores[xl_index]:
            # Expandir
            x_new = (1 + gamma) * xc - gamma * simplex[xh_index]
        elif fxr >= valores[xh_index]:
            # Contraer
            x_new = (1 - beta) * xc + beta * simplex[xh_index]
        elif valores[xg_index] < fxr < valores[xh_index]:
            x_new = (1 + beta) * xc - beta * simplex[xh_index]

        fxnew = funcion_objetivo(x_new)
        simplex[xh_index] = x_new

    return simplex[xl_index]

def generar_simplex1(x0, delta=1):
    """
    Genera el simplex inicial para el método Nelder-Mead.

    Parámetros:
    -----------
    x0 : array_like
        El punto inicial en el espacio de búsqueda.
    delta : float, opcional
        El tamaño del simplex (por defecto es 1).

    Retorna:
    --------
    np.ndarray
        El simplex inicial generado.
    """
    n = len(x0)
    
    alpha1 = ( ( (np.sqrt(n + 1) + (n - 1)) ) / (n * (np.sqrt(2)) ) ) * delta
    alpha2 = ( ( (np.sqrt(n + 1) - 1) ) / (n * np.sqrt(2)) ) * delta
    puntos_simplex = []

    for i in range(n):
        point = [x0[j] + alpha1 if j == i else x0[j] + alpha2 for j in range(n)]
        puntos_simplex.append(point)
    return np.array(puntos_simplex)


def execute_total(fx, p):
    """
    Ejecuta el proceso de optimización y muestra los resultados.

    Parámetros:
    -----------
    fx : función
        La función objetivo que se quiere optimizar.
    p : array_like
        El punto inicial en el espacio de búsqueda.

    Retorna:
    --------
    None
    """
    v_found = Nelder_mead_simplex(fx, p)
    print(f"El punto óptimo encontrado es: {v_found} donde el valor al evaluarlo es {fx(v_found)}")
