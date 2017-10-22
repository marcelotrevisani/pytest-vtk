#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-vtk',
    packages='pytestvtk',
    version='0.1.0',
    author='Marcelo Duarte Trevisani',
    author_email='marceloduartetrevisani@gmail.com',
    maintainer='Marcelo Duarte Trevisani',
    maintainer_email='marceloduartetrevisani@gmail.com',
    license='MIT',
    url='https://github.com/marcelotrevisani/pytest-vtk',
    description='Pytest plugin to easily test the VTK objects from VTK library',
    keywords="pytest test vtk unittest",
    long_description=read('README.rst'),
    install_requires=['pytest>=3.1.1', 'numpy', 'vtk>=7.0.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'pytest-vtk = pytestvtk',
        ],
    },
)
