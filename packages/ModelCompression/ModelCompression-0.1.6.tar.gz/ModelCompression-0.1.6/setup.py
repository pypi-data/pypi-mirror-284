
# Licensed under the MIT license.

import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding='utf-8').read()

setup(
    name = 'ModelCompression',
    version = '0.1.6',
    author = 'AI Team',
    author_email = '710783765@qq.com',
    description = 'Neural Network Compression',
    long_description = read('README.rst'),
    license = 'MIT',
    url = None,

	packages=find_packages('ModelCompression',exclude=["*.ModelZoo"]),
	package_dir = {'':'ModelCompression'},
    python_requires = '>=3.6.2',
    install_requires = [
        'thop',

    ]


)
