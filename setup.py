# -*- coding: utf-8 -*-
"""
Created on Tue Oct  31 15:54:58 2023
A brief comment just to modify the file
@author: Felipe
"""

from setuptools import setup, find_packages
from module_structure import __name__

NAME = __name__

setup(
    name=NAME,
    description='Brief description of your package',
    author_email='felisebas2002@gmail.com',
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
