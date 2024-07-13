from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Paquete de Optimizacion de Python'
LONG_DESCRIPTION = 'Paquete de Optimizacion de Python que contiene métodos de funciones multivariables; directos y de gradiente, y funciones de una sola variable; eliminación de regiones y basados en la derivada'

# Configurando
setup(
    name="paqueteoptimizacion_isa",  
    version=VERSION,
    author="IsabellaJB",
    author_email="isabellajib5@gmail.com",  # Corregido: sin < y >
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[''],  
    keywords=['python', 'optimizacion', 'multivariables', 'variable'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
