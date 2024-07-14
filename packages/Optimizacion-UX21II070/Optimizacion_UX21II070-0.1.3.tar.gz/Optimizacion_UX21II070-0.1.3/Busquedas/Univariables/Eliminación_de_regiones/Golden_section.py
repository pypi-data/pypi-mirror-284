import numpy as np
import random
import matplotlib.pyplot as plt

def Golden_search(fx, a, b, e=0.0000001):
    """
    Implementa el algoritmo de búsqueda dorada para encontrar el mínimo de una función en un intervalo dado.

    El método de búsqueda dorada es una técnica de optimización que busca un mínimo local de una función objetivo utilizando un enfoque de búsqueda basado en la proporción áurea.

    Parámetros
    ----------
    fx : callable
        La función objetivo a minimizar. Debe aceptar un solo argumento (un número) y devolver un valor numérico.
    a : float
        El límite inferior del intervalo de búsqueda.
    b : float
        El límite superior del intervalo de búsqueda.
    e : float, opcional
        El criterio de precisión. La búsqueda se detiene cuando el ancho del intervalo es menor o igual a este valor. El valor predeterminado es 0.0000001.

    Devuelve
    --------
    x_list : list
        Lista de puntos x en los que se evaluó la función durante la búsqueda.
    y_list : list
        Lista de valores de f(x) correspondientes a los puntos x encontrados.

    Ejemplos
    --------
    >>> def f(x):
    ...     return (x - 2)**2
    >>> x_list, y_list = Golden_search(f, 0, 4, 0.01)
    >>> x_list
    [1.618033988749895, 2.381966011250105, 1.5278640450004204, 2.4721359549995796, 1.951057033410827, 2.048942966589173]
    >>> y_list
    [1.618033988749895, 1.618033988749895, 0.272019649514068, 0.272019649514068, 0.0027050871401028287, 0.0027050871401028287]

    Notas
    -----
    El método utiliza la proporción áurea para reducir el intervalo de búsqueda en cada iteración. La precisión de la búsqueda está determinada por el parámetro `e`.
    """
    # Inicializa las variables para el intervalo de búsqueda
    x_list = []
    y_list = []
    
    # Asegura que a es menor que b
    if a > b:
        a, b = b, a
    
    # Calcula las posiciones internas basadas en la proporción áurea
    gr = (np.sqrt(5) + 1) / 2  # Proporción áurea
    c = b - (b - a) / gr
    d = a + (b - a) / gr
    fc = fx(c)
    fd = fx(d)
    
    # Ejecuta el algoritmo hasta que el ancho del intervalo sea menor o igual a la precisión deseada
    while (b - a) > e:
        # Añade los puntos a las listas
        x_list.extend([c, d])
        y_list.extend([fc, fd])
        
        if fc < fd:
            b = d
            d = c
            fd = fc
            c = b - (b - a) / gr
            fc = fx(c)
        else:
            a = c
            c = d
            fc = fd
            d = a + (b - a) / gr
            fd = fx(d)

    # Añade los últimos puntos a las listas
    x_list.extend([c, d])
    y_list.extend([fc, fd])

    return x_list, y_list


def execute_total(fx, epsilon, lm, lM):
    """
    Ejecuta el algoritmo de búsqueda dorada y visualiza los resultados en una gráfica.

    Esta función llama al método `Golden_search` para encontrar los puntos mínimos y grafica la función objetivo junto con
    los puntos mínimos encontrados.

    Parámetros
    ----------
    fx : callable
        La función objetivo a minimizar. Debe aceptar un solo argumento (un número) y devolver un valor numérico.
    epsilon : float
        El criterio de precisión. La búsqueda se detiene cuando el ancho del intervalo es menor o igual a este valor.
    lm : float
        El límite inferior del intervalo de búsqueda para la gráfica.
    lM : float
        El límite superior del intervalo de búsqueda para la gráfica.

    Devuelve
    --------
    None
        La función no retorna valores; en su lugar, muestra una gráfica con los resultados de la búsqueda dorada.

    Ejemplos
    --------
    >>> def f(x):
    ...     return (x - 2)**2
    >>> fig, ax = plt.subplots()
    >>> execute_total(f, 0.01, 0, 4)
    """
    x_vals = np.linspace(lm, lM, 100)  # Genera valores x en el intervalo especificado
    y_vals = fx(x_vals)  # Calcula los valores correspondientes de f(x)

    # Llama al método Golden_search para encontrar los puntos mínimos
    x_p, y_p = Golden_search(fx, lm, lM, epsilon)

    # Dibuja la gráfica de la función objetivo
    plt.plot(x_vals, y_vals, label="Función objetivo")

    # Añade los puntos mínimos encontrados a la gráfica
    plt.scatter(x_p, y_p, color='red', label='Puntos de búsqueda')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Resultado de la Búsqueda Dorada")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()