# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:54:58 2022
A brief comment just to modify the file
@author: Felisebas
"""

from setuptools import setup, find_packages
from MLearning import tensor_calculator


AUTHOR = Felisebas
NAME = tensor_calculator
setup(
    name=tensor_calculator,
    description='Brief description of your package',
    author=Felisebas,
    author_email='pedro.anquela@ufv.es',
    license='MIT',
    python_requires='>=3.9.5',
    packages=find_packages(),
    include_package_data=True,
    package_data={'': ['resources/*.csv', 'resources/clusters/*.csv']},
    install_requires=[
        'pandas',
        'numpy',
        'torch'
    ]
)
