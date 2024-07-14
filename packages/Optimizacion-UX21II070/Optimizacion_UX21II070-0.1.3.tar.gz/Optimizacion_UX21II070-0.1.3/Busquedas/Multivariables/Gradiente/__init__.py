"""
Paquete de funciones de optimización.

Este paquete incluye tres módulos que proporcionan funciones para realizar optimizaciones utilizando métodos matemáticos clásicos.

Módulos disponibles:
--------------------
- `Cauchy`: Contiene la implementación del método de optimización Cauchy basado en el gradiente.
- `Gradiente_conjugado`: Contiene la implementación del método de optimización del gradiente conjugado.
- `Metodo_newton`: Contiene la implementación del método de optimización de Newton.

Importaciones
-------------
Puedes importar funciones y métodos de los módulos como se muestra a continuación:

from optimizacion.Cauchy import gradiante, cauchy, execute_total as execute_cauchy
from optimizacion.Gradiente_conjugado import gradiante, gradiante_conjugado, execute_total as execute_gradiente_conjugado
from optimizacion.Metodo_newton import gradiante, hessian_matrix, Newton, execute_total as execute_newton

Funciones
---------
- `gradiante(f, x, deltaX=0.001)`: Calcula el gradiente de la función `f` en el punto `x` (común en todos los módulos).
- `cauchy(funcion, x0, epsilon1, epsilon2, M, Metodo_busqueda)`: Implementa el algoritmo Cauchy para la optimización.
- `execute_total(funcion, x0, epsilon1, epsilon2, M, Metodo_busqueda)`: Ejecuta el proceso de optimización usando el método Cauchy y muestra los resultados.
- `gradiante_conjugado(funcion, x0, epsilon1, epsilon2, epsilon3, M, Metodo_busqueda)`: Implementa el algoritmo del gradiente conjugado para la optimización.
- `execute_total(funcion, x0, epsilon1, epsilon2, epsilon3, iteraciones, Metodo_busqueda)`: Ejecuta el proceso de optimización usando el método del gradiente conjugado y muestra los resultados.
- `Newton(funcion, x0, epsilon1, epsilon2, M, Metodo_busqueda)`: Implementa el algoritmo de Newton para la optimización.
- `execute_total(funcion, x0, epsilon1, epsilon2, M, Metodo_busqueda)`: Ejecuta el proceso de optimización usando el método de Newton y muestra los resultados.

Ejemplos de uso:
----------------
Para importar funciones específicas desde el paquete:

    from optimizacion.Cauchy import gradiante, execute_total as execute_cauchy
    from optimizacion.Gradiente_conjugado import gradiante, execute_total as execute_gradiente_conjugado
    from optimizacion.Metodo_newton import gradiante, hessian_matrix, execute_total as execute_newton

    # Ejemplo de uso del método Cauchy
    resultado_cauchy = execute_cauchy(funcion_objetivo, punto_inicial, epsilon1, epsilon2, M, metodo_busqueda)

    # Ejemplo de uso del método Gradiente Conjugado
    resultado_gradiente_conjugado = execute_gradiente_conjugado(funcion_objetivo, punto_inicial, epsilon1, epsilon2, epsilon3, iteraciones, metodo_busqueda)

    # Ejemplo de uso del método de Newton
    resultado_newton = execute_newton(funcion_objetivo, punto_inicial, epsilon1, epsilon2, M, metodo_busqueda)
"""

# Importar funciones del módulo `Cauchy`
from .Cauchy import (
    gradiante,
    cauchy,
    execute_total as execute_cauchy
)

# Importar funciones del módulo `Gradiente_conjugado`
from .Gradiente_conjugado import (
    gradiante,
    gradiante_conjugado,
    execute_total as execute_gradiente_conjugado
)

# Importar funciones del módulo `Metodo_newton`
from .Metodo_newton import (
    gradiante,
    hessian_matrix,
    Newton,
    execute_total as execute_newton
)

__all__ = [
    "gradiante",
    "cauchy",
    "execute_cauchy",
    "gradiante_conjugado",
    "execute_gradiente_conjugado",
    "Newton",
    "hessian_matrix",
    "execute_newton"
]
