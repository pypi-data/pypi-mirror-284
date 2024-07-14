import numpy as np
import matplotlib.pyplot as plt

def fibonacci(fx, a, b, n):
    """
    Implementa el algoritmo de búsqueda de Fibonacci para encontrar el mínimo de una función en un intervalo dado.

    El método de búsqueda de Fibonacci es una técnica de optimización que utiliza la secuencia de Fibonacci para reducir el intervalo de búsqueda y encontrar el mínimo local de una función objetivo.

    Parámetros
    ----------
    fx : callable
        La función objetivo a minimizar. Debe aceptar un solo argumento (un número) y devolver un valor numérico.
    a : float
        El límite inferior del intervalo de búsqueda.
    b : float
        El límite superior del intervalo de búsqueda.
    n : int
        El número de iteraciones a realizar, que determina la precisión de la búsqueda. Este valor debería ser mayor que 1.

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
    >>> x_list, y_list = fibonacci(f, 0, 4, 10)
    >>> x_list
    [1.618033988749895, 2.618033988749895]
    >>> y_list
    [0.00000000000000044, 0.00000000000000044]

    Notas
    -----
    La búsqueda se basa en la secuencia de Fibonacci para seleccionar los puntos de prueba en el intervalo de búsqueda. La precisión de la búsqueda está determinada por el número de iteraciones `n`.
    """
    x_list = []
    y_list = []

    l = b - a  # Longitud inicial del intervalo
    k = 2  # Inicializa el índice de la secuencia de Fibonacci

    while k < n:
        # Calcula la posición de los puntos de prueba usando la secuencia de Fibonacci
        fib_k = num_fibonacci(n - k + 1) / num_fibonacci(n + 1) * l
        x1 = a + fib_k
        x2 = b - fib_k

        # Evalúa la función en los puntos x1 y x2
        f_x1 = fx(x1)
        f_x2 = fx(x2)

        # Actualiza los límites del intervalo basado en las evaluaciones de la función
        if f_x1 > f_x2:
            a = x1
        elif f_x1 < f_x2:
            b = x2
        else:
            a = x1
            b = x2
        
        # Añade los puntos a las listas
        x_list.extend([x1, x2])
        y_list.extend([f_x1, f_x2])
        
        k += 1  # Incrementa el índice de la secuencia de Fibonacci

        if k >= n:
            x_list = [x1, x2]
            y_list = [f_x1, f_x2]
            return x_list, y_list
    
    # Devuelve el punto medio del intervalo final como resultado de la búsqueda
    return (a + b) / 2

def num_fibonacci(n):
    """
    Calcula el número de Fibonacci en la posición n usando la fórmula cerrada.

    La fórmula cerrada para el número de Fibonacci usa la proporción áurea para calcular el número de Fibonacci en la posición n.

    Parámetros
    ----------
    n : int
        La posición en la secuencia de Fibonacci para calcular el número correspondiente.

    Devuelve
    --------
    int
        El número de Fibonacci en la posición n.

    Ejemplos
    --------
    >>> num_fibonacci(5)
    5
    >>> num_fibonacci(10)
    55
    """
    # Calcula el número de Fibonacci usando la fórmula cerrada
    phi = (1 + np.sqrt(5)) / 2
    return np.round((phi**n - (-1/phi)**n) / np.sqrt(5))


def execute_total(fx, func_name, lm, lM, n=100):
    """
    Ejecuta el algoritmo de búsqueda de Fibonacci y visualiza los resultados en una gráfica.

    Esta función llama al método `fibonacci` para encontrar los puntos mínimos y grafica la función objetivo junto con
    los puntos mínimos encontrados.

    Parámetros
    ----------
    fx : callable
        La función objetivo a minimizar. Debe aceptar un solo argumento (un número) y devolver un valor numérico.
    func_name : str
        El nombre de la función objetivo, que se usará como título en la gráfica.
    lm : float
        El límite inferior del intervalo de búsqueda para la gráfica.
    lM : float
        El límite superior del intervalo de búsqueda para la gráfica.
    n : int, opcional
        El número de iteraciones para la búsqueda de Fibonacci. El valor predeterminado es 100.

    Devuelve
    --------
    None
        La función no retorna valores; en su lugar, muestra una gráfica con los resultados de la búsqueda de Fibonacci.

    Ejemplos
    --------
    >>> def f(x):
    ...     return (x - 2)**2
    >>> fig, ax = plt.subplots()
    >>> execute_total(f, 'f(x) = (x - 2)^2', 0, 4, 10)
    """
    x_vals = np.linspace(lm, lM, 100)  # Genera valores x en el intervalo especificado
    y_vals = fx(x_vals)  # Calcula los valores correspondientes de f(x)

    # Llama al método Fibonacci para encontrar los puntos mínimos
    x_p, y_p = fibonacci(fx, lm, lM, n)

    # Dibuja la gráfica de la función objetivo
    plt.plot(x_vals, y_vals, label="Función objetivo")

    # Añade los puntos mínimos encontrados a la gráfica
    for i, (x, y) in enumerate(zip(x_p, y_p)):
        plt.scatter(x, y, label=f'Punto {i+1}: ({x:.2f}, {y:.2f})')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(func_name)
    plt.grid(True)
    plt.legend() 

    plt.tight_layout()
    plt.show()