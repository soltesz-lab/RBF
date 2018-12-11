#!/usr/bin/env python
if __name__ == '__main__':
  import numpy as np
  from setuptools import setup
  from setuptools.extension import Extension
  from Cython.Build import cythonize
  ext = []
  ext += [Extension(name='rbf.halton',sources=['rbf/halton.pyx'],include_dirs=[np.get_include()])]
  ext += [Extension(name='rbf.misc.bspline',sources=['rbf/misc/bspline.pyx'],include_dirs=[np.get_include()])]
  ext += [Extension(name='rbf.geometry',sources=['rbf/geometry.pyx'],include_dirs=[np.get_include()])]
  ext += [Extension(name='rbf.poly',sources=['rbf/poly.pyx'],include_dirs=[np.get_include()])]
  setup(name='RBF',
        version='1.2',
        description='Package containing the tools necessary for radial basis function (RBF) applications',
        author='Trever Hines',
        author_email='treverhines@gmail.com',
        url='www.github.com/treverhines/RBF',
        packages=['rbf','rbf.misc'],
        ext_modules=cythonize(ext),
        license='MIT')


