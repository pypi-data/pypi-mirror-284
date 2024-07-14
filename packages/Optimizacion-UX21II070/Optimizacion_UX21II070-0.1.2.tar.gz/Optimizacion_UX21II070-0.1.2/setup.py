from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="Optimizacion_UX21II070",
    version="0.1.2",
    author="Angel Ortega",
    author_email="angel-leonz@hotmail.com",
    description="Un paquete de métodos de optimización para funciones univariables y multivariables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AngelOr31/Optimizacion_proyecto",
    packages=["Funciones_objetivo","Busquedas.Multivariables.Directos","Busquedas.Multivariables.Gradiente",
              "Busquedas.Univariables.Basados_en_derivadas","Busquedas.Univariables.Eliminación_de_regiones"],
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10',
    install_requires=[
        'matplotlib',
        'numpy',
    ],
    project_urls={
        'Documentation': 'https://github.com/AngelOr31/Optimizacion_proyecto/docs',
        'Source': 'https://github.com/AngelOr31/Optimizacion_proyecto',
    },
)
