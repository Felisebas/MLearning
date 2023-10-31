from setuptools import setup, find_packages
from MLearning import _author,version,name_


VERSION = _version_
AUTHOR = _author_
NAME = _name_

setup(
    name                    = NAME,
    version                 = VERSION,
    description             = 'Brief description of your package',
    author                  = AUTHOR,
    author_email            = 'felisebas2002@gmail.com',
    license                 = 'MIT',
    python_requires         = '>=3.9.5',
    packages                = find_packages(),
    include_package_data    = True,
    package_data            = {'': ['resources/.csv','resources/clusters/.csv']},
    install_requires        = [
                                'pandas',
                                'numpy',
                                'torch'
                                ]
     )
                                
