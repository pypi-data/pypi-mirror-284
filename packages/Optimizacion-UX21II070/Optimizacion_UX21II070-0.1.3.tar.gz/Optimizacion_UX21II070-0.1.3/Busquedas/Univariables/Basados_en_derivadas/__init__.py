"""
Paquete para métodos de búsqueda de puntos críticos y optimización de funciones.

Este paquete contiene tres módulos principales para la búsqueda de puntos críticos en funciones matemáticas usando diferentes métodos numéricos: bisección, Newton-Raphson y secante.

Módulos:
--------
1. **biseccion**: Contiene funciones para el cálculo de derivadas y la búsqueda de puntos críticos usando el método de la bisección.
2. **newton_raphson**: Incluye funciones para el cálculo de derivadas y la búsqueda de puntos críticos usando el método de Newton-Raphson.
3. **secante**: Ofrece funciones para el cálculo de derivadas y la búsqueda de puntos críticos usando el método de la secante.

Submódulos:
-----------
- **biseccion**:
    - `central_difference_first(f, x)`: Calcula la primera derivada de la función `f` en el punto `x` usando diferencias centrales.
    - `Biseccion(fx, a, b, e)`: Encuentra puntos críticos de la función `fx` en el intervalo `[a, b]` utilizando el método de la bisección.
    - `execute_total(fx, epsilon, lm, lM)`: Ejecuta el proceso de búsqueda de puntos críticos en el intervalo `[lm, lM]` y grafica la función `fx`.

- **newton_raphson**:
    - `central_difference_first(f, x, delta=0.0001)`: Calcula la primera derivada de la función `f` en el punto `x` usando diferencias centrales.
    - `central_difference_second(f, x, delta=0.0001)`: Calcula la segunda derivada de la función `f` en el punto `x` usando diferencias centrales.
    - `newton_raphson(f, lm, epsilon, max_iterations=100)`: Encuentra puntos críticos de la función `f` comenzando en el punto `lm` utilizando el método de Newton-Raphson.
    - `execute_total(fx, epsilon, lm, lM)`: Ejecuta el proceso de búsqueda de puntos críticos en el intervalo `[lm, lM]` y grafica la función `fx`.

- **secante**:
    - `central_difference_first(f, x)`: Calcula la primera derivada de la función `f` en el punto `x` usando diferencias centrales.
    - `secante(fx, a, b, e)`: Encuentra puntos críticos de la función `fx` en el intervalo `[a, b]` utilizando el método de la secante.
    - `execute_total(fx, epsilon, lm, lM)`: Ejecuta el proceso de búsqueda de puntos críticos en el intervalo `[lm, lM]` y grafica la función `fx`.
"""

# Importar funciones desde los módulos
from .Biseccion import central_difference_first, Biseccion, execute_total as biseccion_execute_total
from .Newton_raphson import central_difference_first as newton_raphson_central_difference_first, \
                            central_difference_second, newton_raphson, execute_total as newton_raphson_execute_total
from .Secante import central_difference_first as secante_central_difference_first, \
                     secante, execute_total as secante_execute_total

__all__ = [
    'central_difference_first',
    'Biseccion',
    "biseccion_execute_total",
    'newton_raphson_central_difference_first',
    'central_difference_second',
    'newton_raphson',
    'newton_raphson_execute_total',
    'secante_central_difference_first',
    'secante',
    'secante_execute_total'
]
