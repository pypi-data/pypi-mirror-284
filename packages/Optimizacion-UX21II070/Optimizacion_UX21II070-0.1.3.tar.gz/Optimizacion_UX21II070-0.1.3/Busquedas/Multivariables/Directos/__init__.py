"""
Paquete de funciones de optimización.

Este paquete incluye dos módulos que proporcionan funciones para realizar optimizaciones utilizando métodos matemáticos clásicos.

Módulos disponibles:
--------------------
- `hooke_jeeves`: Contiene la implementación del método de optimización Hooke-Jeeves.
- `nelder_mead`: Contiene la implementación del método de optimización Nelder-Mead Simplex.

Importaciones
-------------
Puedes importar funciones y métodos de los módulos como se muestra a continuación:

from optimizacion.hooke_jeeves import hooke_jeeves, exploratory_move, execute_total as execute_hooke_jeeves
from optimizacion.nelder_mead import Nelder_mead_simplex, generar_simplex1, execute_total as execute_nelder_mead

Funciones
---------
- `hooke_jeeves(fx, p, delta, alpha=2, epsilon=1e-6)`: Implementa el algoritmo Hooke-Jeeves para la optimización.
- `exploratory_move(fx, xc, d, puntos)`: Realiza un movimiento exploratorio en el espacio de búsqueda para el método Hooke-Jeeves.
- `execute_total(fx, p, delta)`: Ejecuta el proceso de optimización usando el método Hooke-Jeeves y muestra los resultados.
- `Nelder_mead_simplex(funcion_objetivo, p, gamma=2, beta=0.5, epsilon=1e-3)`: Implementa el algoritmo Nelder-Mead Simplex para la optimización.
- `generar_simplex1(x0, delta=1)`: Genera el simplex inicial para el método Nelder-Mead.
- `execute_total(fx, p)`: Ejecuta el proceso de optimización usando el método Nelder-Mead y muestra los resultados.

Ejemplos de uso:
----------------
Para importar funciones específicas desde el paquete:

    from optimizacion.hooke_jeeves import hooke_jeeves, execute_total as execute_hooke_jeeves
    from optimizacion.nelder_mead import Nelder_mead_simplex, execute_total as execute_nelder_mead

    # Ejemplo de uso del método Hooke-Jeeves
    resultado_hooke_jeeves = execute_hooke_jeeves(funcion_objetivo, punto_inicial, delta_inicial)

    # Ejemplo de uso del método Nelder-Mead
    resultado_nelder_mead = execute_nelder_mead(funcion_objetivo, punto_inicial)

"""

# Importar funciones del módulo `hooke_jeeves`
from .Hooke_Jeeves import (
    hooke_jeeves, 
    exploratory_move, 
    execute_total as execute_hooke_jeeves
)

# Importar funciones del módulo `nelder_mead`
from .Nelder_Mead import (
    Nelder_mead_simplex, 
    generar_simplex1, 
    execute_total as execute_nelder_mead
)

__all__ = [
    "hooke_jeeves",
    "exploratory_move",
    "execute_hooke_jeeves",
    "Nelder_mead_simplex",
    "generar_simplex1",
    "execute_nelder_mead"
]
