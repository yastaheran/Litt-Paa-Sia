# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 13:33:56 2016

@author: YasTah
"""
#!/usr/bin/env python

from distutils.core import setup, Extension
from Cython.Distutils import build_ext

setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("mandelbrot", ["mandelbrot_3.pyx"])]
)
