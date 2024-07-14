# Optimización UX21II070

debido a gith tiene un archivo que ignora lo creado por setup.py sdits(archivos que se suben a Pypi) es normal que no se encuentren adjuntos(breve aclaración)

Este proyecto de optimización se enfoca en implementar y documentar diversos métodos de optimización tanto para funciones de una variable como para funciones multivariadas, todos estos métodos fueron vistos durante la clase. 

## Estructura del Proyecto

El proyecto está organizado en las siguientes carpetas y archivos principales:

Optimizacion_proyecto/
│
├── Busquedas
│ ├── Multivariables
│ │ ├── Directos
│ │ │ ├── Hooke_Jeeves.py
│ │ │ ├── Nelder_Mead.py
│ │ │ └── init.py
│ │ └── Gradiente
│ │ │ ├── Cauchy.py
│ │ │ ├── Gradiente_conjugado.py
│ │ │ ├── Metodo_newton.py
│ │ │ └── init.py
│ ├── Univariables
│ │ ├── Basados_en_derivadas
│ │ │ ├── Biseccion.py
│ │ │ ├── Newthon_rapshon.py
│ │ │ ├── Secante.py
│ │ │ └── init.py
│ │ └── Eliminación_de_regiones
│ │ │ ├── Bounding_phase.py
│ │ │ ├── Golden_section.py
│ │ │ ├── Search_Fibonacci.py
│ │ │ └── init.py
│ └── metodos.py
│
├── Funciones_objetivo
│ ├── init.py
│ ├── sin_restricciones.py
│ └── con_restricciones.py


## Instalación

Para instalar este paquete, puedes usar pip:
