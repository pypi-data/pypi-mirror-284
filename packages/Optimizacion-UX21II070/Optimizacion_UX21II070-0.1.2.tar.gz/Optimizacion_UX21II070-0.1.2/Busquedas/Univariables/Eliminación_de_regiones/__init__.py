# __init__.py

"""
Paquete de Métodos de Optimización

Este paquete incluye varias técnicas de optimización para encontrar el mínimo de una función objetivo. 

Módulos
-------
- `bounding_phase`: Implementa el método Bounding Phase para encontrar un mínimo local de una función.
- `Golden_search`: Implementa el algoritmo de búsqueda dorada para encontrar el mínimo de una función en un intervalo dado.
- `Search_fibonacci`: Implementa el algoritmo de búsqueda de Fibonacci para encontrar el mínimo de una función usando la secuencia de Fibonacci.

Funciones
---------
Cada módulo incluye dos funciones principales:
- Una función de optimización para buscar el mínimo.
- Una función `execute_total` para ejecutar la optimización y visualizar los resultados en una gráfica.

Ejemplos de uso:
----------------
>>> from optimizacion import bounding_phase, Golden_search, Search_fibonacci

>>> def f(x):
...     return (x - 2)**2

>>> # Uso del método Bounding Phase
>>> x_list, y_list = bounding_phase(f, [0], 0.1, -10, 10)
>>> print(x_list)
>>> print(y_list)

>>> # Uso del método de Búsqueda Dorada
>>> x_list, y_list = Golden_search(f, 0, 4, 0.01)
>>> print(x_list)
>>> print(y_list)

>>> # Uso del método de Búsqueda de Fibonacci
>>> x_list, y_list = fibonacci(f, 0, 4, 10)
>>> print(x_list)
>>> print(y_list)

"""

from .Bounding_phase import bounding_phase, execute_total as bounding_phase_execute_total
from .Golden_section import Golden_search, execute_total as golden_search_execute_total
from .Search_Fibonacci import fibonacci, execute_total as fibonacci_execute_total

__all__ = [
    "bounding_phase",
    "bounding_phase_execute_total",
    "Golden_search",
    "golden_search_execute_total",
    "fibonacci",
    "fibonacci_execute_total",
]
