import matplotlib.pyplot as plt
import numpy as np

def bounding_phase(f, valor_i, delta, lm, lM):
    """
    Realiza la optimización usando el método Bounding Phase para encontrar el mínimo de una función.

    Este método busca un mínimo local para una función objetivo dada, ajustando dinámicamente el intervalo de búsqueda
    hasta encontrar un mínimo en el intervalo especificado.

    Parámetros
    ----------
    f : callable
        La función objetivo que se desea minimizar. Debe aceptar un solo argumento y devolver un valor numérico.
    valor_i : list
        Valor inicial para la búsqueda del mínimo. Debe ser una lista con un solo valor que sirve como punto de partida.
    delta : float
        El incremento de búsqueda. Este valor define el tamaño del paso durante la búsqueda del mínimo.
    lm : float
        El límite inferior del intervalo de búsqueda. Define el rango inferior dentro del cual se busca el mínimo.
    lM : float
        El límite superior del intervalo de búsqueda. Define el rango superior dentro del cual se busca el mínimo.

    Retorna
    -------
    x_array : np.ndarray
        Array de puntos x encontrados durante la búsqueda, donde se han encontrado valores mínimos locales.
    y_array : np.ndarray
        Array de valores de f(x) correspondientes a los puntos x encontrados.

    Ejemplos
    --------
    >>> def f(x):
    ...     return (x - 2)**2
    >>> x_array, y_array = bounding_phase(f, [0], 0.1, -10, 10)
    Punto encontrado 1: x = 1.8999999999999995, f(x) = 0.010000000000000106
    Punto encontrado 2: x = 1.9999999999999996, f(x) = 1.9721522630525295e-31
    >>> x_array
    array([1.9, 2. ])
    >>> y_array
    array([1.00000000e-02, 1.97215226e-31])

    Notes
    -----
    Si no se encuentran puntos válidos dentro de los límites especificados, la función imprimirá un mensaje y retornará arrays vacíos.
    """
    k = 0
    x = valor_i[0] + .35  # Inicializa x con un valor ligeramente desplazado del valor inicial
    x_list = []
    y_list = []
    delta_p = False  # Bandera para verificar el crecimiento de delta positivo
    delta_n = False  # Bandera para verificar el crecimiento de delta negativo

    # Ajusta el valor inicial de x si x - delta o x + delta resultan en 0
    while (x - delta) == 0 or (x + delta) == 0:
        x = x + .1

    # Busca el intervalo de búsqueda donde se encuentra un mínimo
    while not delta_p and not delta_n:
        md = x - abs(delta)
        Md = x + abs(delta)
        f_md = f(md)
        f_Md = f(Md)
        fx = f(x)

        if f_md >= fx and fx >= f_Md:
            delta_p = True
            if delta < 0:
                delta = delta * -1
        elif f_md <= fx and fx <= f_Md:
            delta_n = True
            if delta > 0:
                delta = delta * -1

        if not delta_p and not delta_n:
            x = x + .1
            while (x - delta) == 0 or (x + delta) == 0:
                x = x + .1

    fx_next = -1
    fx = 0

    # Busca un mínimo local moviendo el punto x
    while fx_next < fx:
        x_next = x + 1 ** k * delta

        if x < lm or x > lM:
            if len(x_list) == 0:
                print("No se encontraron puntos dentro del intervalo especificado.")
            return np.array([]), np.array([])

        fx = f(x)
        fx_next = f(x_next)

        if fx_next < fx:
            k += 1
            x_anterior = x
            x = x_next

            x_list = [x_anterior, x]
            y_list = [f(x_anterior), f(x)]

    print(f"Punto encontrado 1: x = {x_anterior}, f(x) = {f(x_anterior)}")
    print(f"Punto encontrado 2: x = {x}, f(x) = {f(x)}")

    return np.array(x_list), np.array(y_list)


def execute_total(fx, lm, lM, delta):
    """
    Ejecuta la función de optimización y visualiza los resultados en una gráfica, siendo todo en uno.

    Esta función llama al método `bounding_phase` para encontrar los puntos mínimos y grafica la función objetivo junto con
    los puntos mínimos encontrados.

    Parámetros
    ----------
    fx : callable
        La función objetivo a minimizar. Debe aceptar un solo argumento y devolver un valor numérico.
    lm : float
        El límite inferior del intervalo de búsqueda para la gráfica.
    lM : float
        El límite superior del intervalo de búsqueda para la gráfica.
    delta : float
        El incremento de búsqueda usado en el método Bounding Phase.

    Retorna
    -------
    None
        La función no retorna valores; en su lugar, muestra una gráfica con los resultados.

    Examples
    --------
    >>> def f(x):
    ...     return (x - 2)**2
    >>> fig, ax = plt.subplots()
    >>> execute_total(ax, f, -10, 10, 0.1)
    """
    x_vals = np.linspace(lm, lM, 100)  # Genera valores x en el intervalo especificado
    y_vals = fx(x_vals)  # Calcula los valores correspondientes de f(x)

    # Llama a la función bounding_phase para encontrar los puntos mínimos
    x_p, y_p = bounding_phase(fx, [lm], delta, lm, lM)

    if len(x_p) == 0:
        plt.plot(x_vals, y_vals, label="No hay puntos críticos en este rango")
    else:
        plt.plot(x_vals, y_vals, label="Función objetivo")
        for i, (x, y) in enumerate(zip(x_p, y_p)):
            plt.scatter(x, y, label=f'Punto {i+1}: ({x:.2f}, {y:.2f})')

    plt.set_xlabel('x')
    plt.set_ylabel('y')
    plt.set_title("Resultado de la Optimización")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()
