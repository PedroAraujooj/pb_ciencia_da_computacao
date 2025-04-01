from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize



soma_vetor_parallel = Extension(
    'soma_vetor_parallel',
    ['soma_vetor_parallel.pyx'],
    extra_compile_args=['-fopenmp'],
    extra_link_args=['-fopenmp'])

setup(
    name='soma_vetor_parallel',
    ext_modules=cythonize([soma_vetor_parallel], compiler_directives={'language_level': 3})
)