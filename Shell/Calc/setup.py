#!/usr/bin/env python

from distutils.core import setup

__author__ = 'yast@student.matnat.uio.no'

__version__ = '1'

setup(name='rpn',
    version= __version__,
    description='A python RPN calculator',
    author='Yas Taheranpour',
    author_email='yast@student.matnat.uio.no',
    py_modules=['rpn'],
    scripts=['scripts/rpn']
)
