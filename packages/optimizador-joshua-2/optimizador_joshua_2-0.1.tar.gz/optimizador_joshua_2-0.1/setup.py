from setuptools import setup, find_packages

setup(
    name='optimizador_joshua_2',
    version='0.1',
    author="Joshua Rodriguez",
    author_email="joshuarl03@hotmail.com",
    description="Es un paquete enfocado a la optimizacion de variables de diversas maneras",
    packages=find_packages(),
    install_requires=[
        'numpy',
        # Agrega otras dependencias aquí si las tienes
    ],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)