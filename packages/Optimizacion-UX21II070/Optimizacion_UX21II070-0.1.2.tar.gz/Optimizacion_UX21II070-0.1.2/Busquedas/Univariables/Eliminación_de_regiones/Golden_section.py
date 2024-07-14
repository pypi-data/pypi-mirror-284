import numpy as np
import random
import matplotlib.pyplot as plt


def Golden_search(fx, a, b, e):
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
    e : float
        El criterio de precisión. La búsqueda se detiene cuando el ancho del intervalo es menor o igual a este valor.

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
    [2.309430177, 1.690569823]
    >>> y_list
    [1.308752132, 1.308752132]

    Notas
    -----
    El método utiliza la proporción áurea para reducir el intervalo de búsqueda en cada iteración. La precisión de la búsqueda está determinada por el parámetro `e`.
    """
    x_list = []
    y_list = []

    # Inicializa las variables para el intervalo de búsqueda
    aw = random.uniform(a, b)
    bw = random.uniform(a, b)

    # Asegura que el intervalo de búsqueda esté en orden correcto
    while aw > bw:
        aw = random.uniform(a, b)
        bw = random.uniform(a, b)

    k = 1
    lw = 15  # Ancho inicial del intervalo de búsqueda

    # Ejecuta el algoritmo hasta que el ancho del intervalo sea menor o igual a la precisión deseada
    while lw > e:
        lw = bw - aw

        # Calcula los puntos w1 y w2 usando la proporción áurea
        w1 = aw + 0.618 * lw
        w2 = bw - 0.618 * lw

        # Calcula los valores de x en el intervalo [a, b]
        x1 = w1 * (b - a) + a
        x2 = w2 * (b - a) + a

        # Evalúa la función en los puntos x1 y x2
        fw1 = fx(x1)
        fw2 = fx(x2)

        # Actualiza los límites del intervalo basado en las evaluaciones de la función
        if fw1 > fw2:
            aw = x1
        elif fw1 < fw2:
            bw = x2
        else:
            aw = x1
            bw = x2

        # Añade los puntos a las listas
        x_list.extend([x1, x2])
        y_list.extend([fw1, fw2])

        # Incrementa el contador de iteraciones
        k += 1

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
    for i, (x, y) in enumerate(zip(x_p, y_p)):
        plt.scatter(x, y, label=f'Punto {i+1}: ({x:.2f}, {y:.2f})')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Resultado de la Búsqueda Dorada")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()
