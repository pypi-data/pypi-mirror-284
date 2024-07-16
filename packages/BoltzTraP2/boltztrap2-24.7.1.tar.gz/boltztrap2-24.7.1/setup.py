# -*- coding: utf-8 -*-
#    BoltzTraP2, a program for interpolating band structures and calculating
#                semi-classical transport coefficients.
#    Copyright (C) 2017-2024 Georg K. H. Madsen <georg.madsen@tuwien.ac.at>
#    Copyright (C) 2017-2024 Jesús Carrete <jesus.carrete.montana@tuwien.ac.at>
#    Copyright (C) 2017-2024 Matthieu J. Verstraete <matthieu.verstraete@ulg.ac.be>
#    Copyright (C) 2018-2019 Genadi Naydenov <gan503@york.ac.uk>
#    Copyright (C) 2020 Gavin Woolman <gwoolma2@staffmail.ed.ac.uk>
#    Copyright (C) 2020 Roman Kempt <roman.kempt@tu-dresden.de>
#    Copyright (C) 2022 Robert Stanton <stantor@clarkson.edu>
#
#    This file is part of BoltzTraP2.
#
#    BoltzTraP2 is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    BoltzTraP2 is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with BoltzTraP2.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import print_function

import contextlib
import glob
import os
import os.path
import platform
import shutil
import subprocess
import sys
import tempfile
from sysconfig import get_config_vars

import setuptools
from setuptools import Command, Extension, setup
from setuptools.command.build_ext import build_ext as DefaultBuildExtCommand

try:
    # Numpy is the only scientific package required by the setup script itself
    import numpy as np
except ImportError:
    print(
        """Error: numpy is not installed.
Please install it using your package manager or with "pip install numpy".
""",
        file=sys.stderr,
        end="",
    )
    sys.exit(1)

# Set this to True to regenerate BoltzTraP2/sphere/frontend.cpp fron its
# Cython sources as part of the build process.
USE_CYTHON = True

# Extra header and library dirs for compiling the C and C++ source files.
INCLUDE_DIRS = []
LIBRARY_DIRS = []


def has_flag(compiler, flagname):
    "Check whether the compiler supports a particular flag."
    print("About to test the compiler flag {}".format(flagname))
    with tempfile.NamedTemporaryFile("w", suffix=".cpp") as f:
        f.write("int main (int argc, char **argv) { return 0; }")
        try:
            compiler.compile([f.name], extra_postargs=[flagname])
        except setuptools.distutils.errors.CompileError:
            print("The flag {} is NOT supported".format(flagname))
            return False
    print("The flag {} is supported".format(flagname))
    return True


@contextlib.contextmanager
def dir_context(dn):
    """Create a context with a given directory as the CWD."""
    # Sabe the original CWD.
    original = os.getcwd()
    try:
        # Change to the new directory and return control.
        os.chdir(dn)
        yield
    finally:
        # Change back to the original directory.
        os.chdir(original)


class CleanSPGlibCommand(Command):
    """Custom command used to clean the spglib directory."""

    description = "remove libsymspg.a and all old spglib build directores"
    user_options = []

    def initialize_options(self):
        """Do nothing."""
        pass

    def finalize_options(self):
        """Do nothing."""
        pass

    def run(self):
        """Remove libsymspg.a and all spglib build directores."""
        self.announce("About to remove libsymspg.a", level=1)
        try:
            os.remove(BuildSPGlibCommand.static_library)
        except FileNotFoundError:
            self.announce("libsymspg.a did not exist", level=1)
        self.announce(
            "About to remove all old spglib build directories", level=1
        )
        with dir_context(BuildSPGlibCommand.base_dir):
            build_dirs = [i for i in glob.glob("build-*") if os.path.isdir(i)]
            for d in build_dirs:
                shutil.rmtree(d, ignore_errors=True)


class BuildSPGlibCommand(Command):
    """Custom command used to compile spglib."""

    description = "compile a local static copy of spglib"
    user_options = []
    base_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "external", "spglib-1.9.9")
    )
    header_dir = os.path.join(base_dir, "src")
    static_library = os.path.join(base_dir, "libsymspg.a")

    def initialize_options(self):
        """Do nothing."""
        pass

    def finalize_options(self):
        """Do nothing."""
        pass

    def run(self):
        """Run cmake with the right options, and then run make."""
        if os.path.isfile(BuildSPGlibCommand.static_library):
            self.announce("libsymspg.a exists, no need to rebuild it", level=1)
            return
        self.announce(
            "About to create a new build directory for spglib", level=1
        )
        build_dir = tempfile.mkdtemp(
            prefix="build-", dir=BuildSPGlibCommand.base_dir
        )
        self.announce("About to run 'cmake' for spglib", level=1)
        with dir_context(build_dir):
            subprocess.check_call(
                ["cmake", "-DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON", ".."]
            )
        self.announce("About to run 'make' for spglib", level=1)
        with dir_context(build_dir):
            subprocess.check_call(["make"])
            shutil.copy2("libsymspg.a", BuildSPGlibCommand.base_dir)
        self.announce("About to remove the spglib build directory", level=1)
        shutil.rmtree(build_dir)


class BuildExtCommand(DefaultBuildExtCommand):
    """Custom build_ext command that will build spglib first."""

    # these flags are not checked and always added
    required_compile_flags = ["-std=c++11"]
    system_specific_flags = {"Darwin": ["-stdlib=libc++"]}

    def build_extensions(self):
        self.announce("About to test compiler flags")
        # only add flags which pass the flag_filter
        opts = self.required_compile_flags
        for system, compile_flags in self.system_specific_flags.items():
            if platform.system() == system:
                opts += [
                    i for i in compile_flags if has_flag(self.compiler, i)
                ]
        for ext in self.extensions:
            ext.extra_compile_args = opts
        DefaultBuildExtCommand.build_extensions(self)

    def run(self):
        """Run build_spglib and then delegate on the normal build_ext."""
        self.run_command("build_spglib")
        DefaultBuildExtCommand.run(self)


if USE_CYTHON:
    from Cython.Build import cythonize

    extension = "pyx"
else:
    extension = "cpp"

eigen_dir = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), "external", "eigen-eigen-3215c06819b9"
    )
)

extensions = [
    Extension(
        "BoltzTraP2.sphere.frontend",
        [
            "BoltzTraP2/sphere/frontend." + extension,
            "BoltzTraP2/sphere/backend.cpp",
        ],
        language="c++",
        include_dirs=INCLUDE_DIRS
        + [np.get_include(), BuildSPGlibCommand.header_dir, eigen_dir],
        library_dirs=LIBRARY_DIRS,
        runtime_library_dirs=LIBRARY_DIRS,
        extra_objects=[BuildSPGlibCommand.static_library],
    )
]

if USE_CYTHON:
    extensions = cythonize(extensions)

setup(
    name="BoltzTraP2",
    description="band-structure interpolator and transport coefficient"
    " calculator",
    long_description="""BoltzTraP2 provides a numerically stable and efficient method for obtaining
analytic representations of electronic bands based on density-functional-theory
results for relatively sparse grids. It achieves this goal by using smoothed
Fourier interpolation.

BoltzTraP2 can be used as a Python module or as a standalone command-line
program. One of its most frequent use cases involves determining the Onsager
electronic transport coefficients by direct integration over the Brillouin zone
based on the interpolated band structure, as functions of temperature and
chemical potential. This functionality is easy to access in BoltzTraP2, which
also includes many additional features for band-structure analysis, such as
a 3D viewer of the Fermi surface.

The program and the method are described in detail in the following reference:
G. Madsen, J. Carrete & M. J. Verstraete, Comput. Phys. Commun.
""",
    version="24.7.1",
    author="Georg K. H. Madsen",
    author_email="georg.madsen@tuwien.ac.at",
    license="GPLv3+",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: C++",
        "License :: OSI Approved :: GNU General Public License v3 or"
        " later (GPLv3+)",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Chemistry",
    ],
    keywords="electronic band structure Onsager thermoelectric coefficients",
    packages=["BoltzTraP2", "BoltzTraP2.sphere"],
    entry_points={
        "console_scripts": ["btp2 = BoltzTraP2.interface:btp2_main"]
    },
    ext_modules=extensions,
    cmdclass={
        "build_ext": BuildExtCommand,
        "build_spglib": BuildSPGlibCommand,
        "clean_spglib": CleanSPGlibCommand,
    },
    install_requires=[
        "spglib",
        "numpy<2.0",
        "scipy",
        "matplotlib",
        "ase",
        "netCDF4",
        "cython",
    ],
    python_requires=">=3.5",
    url="https://www.boltztrap.org",
    download_url=(
        "https://gitlab.com/sousaw/BoltzTraP2/"
        "repository/archive.tar.gz?ref="
        "v24.1.1"
    ),
)
