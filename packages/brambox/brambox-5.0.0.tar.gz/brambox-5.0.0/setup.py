import glob
import os
import sys

import setuptools as setup
from pkg_resources import DistributionNotFound, get_distribution
from setuptools.extension import Extension

# Versioneer
try:
    import versioneer
except ImportError:
    # we have a versioneer.py file living in the same directory as this file, but
    # if we're using pep 517/518 to build from pyproject.toml its not going to find it
    # https://github.com/python-versioneer/python-versioneer/issues/193#issue-408237852
    # make this work by adding this directory to the python path
    sys.path.append(os.path.dirname(os.path.realpath(__file__)))
    import versioneer

# Cython
try:
    import numpy
    from Cython.Build import cythonize
except ImportError:
    CYTHON = False
    CDEBUG = False
    include_dirs = []
else:
    CYTHON = os.getenv('CYTHON', '0').strip() != '0'  # Generate .c from .pyx with cython
    CDEBUG = os.getenv('CDEBUG', '0').strip() != '0'  # Enable profiling and linetrace in cython files for debugging
    include_dirs = [numpy.get_include()]


def get_dist(pkgname):
    try:
        return get_distribution(pkgname)
    except DistributionNotFound:
        return None


def find_packages():
    return ['brambox'] + ['brambox.' + p for p in setup.find_packages('brambox')]


def find_extensions():
    ext = '.pyx' if CYTHON else '.cpp'
    files = list(glob.glob('brambox/**/*' + ext, recursive=True))

    if os.name == 'nt':
        names = [os.path.splitext(f)[0].replace('\\', '.') for f in files]
        base_compile_args = ['/std:c++14', '/wd4018']
        debug_compile_args = ['/Od']
        build_compile_args = ['/O2']
    else:
        names = [os.path.splitext(f)[0].replace('/', '.') for f in files]
        base_compile_args = ['-std=c++14', '-Wno-sign-compare']
        debug_compile_args = ['-O0']
        build_compile_args = ['-O3']

    if CYTHON and CDEBUG:
        extensions = [
            Extension(
                n,
                [f],
                extra_compile_args=[*base_compile_args, *debug_compile_args],
                define_macros=[('CYTHON_TRACE', '1'), ('CYTHON_TRACE_NOGIL', '1'), ('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
                include_dirs=include_dirs,
            )
            for n, f in zip(names, files)
        ]
    else:
        extensions = [
            Extension(
                n,
                [f],
                extra_compile_args=[*base_compile_args, *build_compile_args],
                define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')],
                include_dirs=include_dirs,
            )
            for n, f in zip(names, files)
        ]

    if CYTHON:
        extensions = (
            cythonize(extensions, gdb_debug=True, compiler_directives={'linetrace': True, 'binding': True}) if CDEBUG else cythonize(extensions)
        )

    return extensions


setup.setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    ext_modules=find_extensions(),
    include_dirs=include_dirs,
    test_suite='test',
)
