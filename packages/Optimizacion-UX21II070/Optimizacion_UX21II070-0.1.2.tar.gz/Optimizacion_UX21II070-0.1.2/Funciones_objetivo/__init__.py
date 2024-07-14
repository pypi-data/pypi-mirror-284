"""
Paquete de funciones de optimización y visualización.

Este paquete incluye dos módulos que proporcionan diversas funciones matemáticas
utilizadas en problemas de optimización, así como métodos para graficar estas funciones en 3D.

Módulos disponibles:
--------------------
- `con_restricciones`: Contiene funciones de prueba de optimización con diversas restricciones
  y métodos para graficar estas funciones.
- `sin_restricciones`: Contiene funciones de prueba de optimización sin restricciones
  y métodos para graficar estas funciones.

Importaciones
-------------
Puedes importar funciones y métodos de los módulos como se muestra a continuación:

from funciones_objetivo import rastrigin, ackley, sphere, rosenbrock, beale, goldstein_price, booth, bukin_n6, matyas, levi_n13, himmelblau, camello_tres_jorobas, easom, cross_in_tray, graficar_funcion, graficar

Funciones
---------
- `rastrigin(x)`: Función de Rastrigin, conocida por su paisaje con múltiples óptimos locales.
- `ackley(x, y=1)`: Función de Ackley, una función multimodal con un único óptimo global.
- `sphere(x)`: Función de Esfera, una función unimodal con un único óptimo global.
- `rosenbrock(x)`: Función de Rosenbrock, utilizada para probar algoritmos de optimización en problemas de minimización no lineales.
- `beale(x, y=1)`: Función de Beale, un problema de optimización no lineal con un óptimo global.
- `goldstein_price(x, y=1)`: Función de Goldstein-Price, una función con varios óptimos locales y globales.
- `booth(x, y=1)`: Función de Booth, una función de prueba simple para problemas de optimización.
- `bukin_n6(x, y=1)`: Función Bukin N.6, un problema de prueba con un paisaje de optimización desafiante.
- `matyas(x, y=1)`: Función de Matyas, una función multimodal con un óptimo global.
- `levi_n13(x, y=1)`: Función Levi N.13, una función de prueba con un paisaje de múltiples óptimos.
- `himmelblau(x, y=1)`: Función de Himmelblau, una función de prueba con múltiples óptimos locales y globales.
- `camello_tres_jorobas(x, y=1)`: Función del Camello de Tres Jorobas, un problema de prueba con un paisaje de optimización complejo.
- `easom(x, y=1)`: Función de Easom, un problema de optimización con un único óptimo global.
- `cross_in_tray(x, y=1)`: Función Cross-in-Tray, una función de prueba con un paisaje complicado para algoritmos de optimización.

Métodos
-------
- `graficar_funcion(funcion, rango_x, rango_y, titulo)`: Grafica una función matemática en 3D para un rango dado de valores en las dimensiones x e y.
- `graficar(funcion_nombre)`: Selecciona y grafica una función matemática predefinida en 3D usando el nombre de la función.

Ejemplos de uso:
----------------
Para importar funciones específicas desde el paquete:

    from funciones_objetivo import rastrigin, graficar

    # Ejemplo de uso
    resultado_rastrigin = rastrigin([1, 2, 3])
    graficar("Rastrigin")
"""

# Importar funciones del módulo `con_restricciones`
from .con_restricciones import (
    graficar_funcion, gomez_levy, graficar, simionescu, townsend, pajaro_mishra, rosenbrock
)

# Importar funciones del módulo `sin_restricciones`
from .sin_restricciones import (
    rastrigin, ackley, sphere, rosenbrock, beale, goldstein_price, booth, bukin_n6, matyas, levi_n13, himmelblau, camello_tres_jorobas, easom,
    cross_in_tray, graficar, graficar_funcion

)

__all__ = [
    "pajaro_mishra",
    "townsend",
    "simionescu",
    "gomez_levy",
    'rastrigin',
    'ackley',
    'sphere',
    'rosenbrock',
    'beale',
    'goldstein_price',
    'booth',
    'bukin_n6',
    'matyas',
    'levi_n13',
    'himmelblau',
    'camello_tres_jorobas',
    'easom',
    'cross_in_tray',
    'graficar_funcion',
    'graficar',
    'graficar_funcion_sin_restricciones',
    'graficar_sin_restricciones',
]
