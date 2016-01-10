#!/usr/bin/env python

import os
from setuptools import setup
from distutils.command.build import build
from distutils.command.install import install
from subprocess import call

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


class FastQZipBuild(build):
    """
    Compiles and builds all the compression tools mentioned in the Makefile
    """

    def run(self):
        print("Calling make during setup.py build")
        # run original build code
        build.run(self)

        build_path = os.path.abspath(self.build_temp)
        cmd = ['make',
        'DEST=' + BASE_PATH,
        'TMP=' + build_path]

        def compile():
            call(cmd, cwd=BASE_PATH)

        self.execute(compile, [], 'Compiling FASTQ compression and decompression libraries.')


class FastQZipInstall(install):
   def initialize_options(self):
       install.initialize_options(self)
       self.build_scripts = None

   def finalize_options(self):
       install.finalize_options(self)
       self.set_undefined_options('build', ('build_scripts', 'build_scripts'))

   def run(self):
        # run original install code
        print("Installation Lib :" + self.install_lib)
        install.run(self)

        self.copy_tree(self.build_lib, self.install_lib)

        print("Build Lib :" + self.build_lib)

# Setup the compression library
setup(
    # Add in all the details for the application
    # Application name:
    name="fastq_comp",

    # Version number (initial):
    version="0.0.1",

    # Application author details:
    author="adasgt",
    author_email="abhiram.das@gmail.com",

    # Packages
    packages=["fastq_comp", "test"],

    # Include additional files into the package
    include_package_data=True,
    test_suite='test',
    # Details
    url="https://github.com/adasgt/fastq_comp",

    #
    license="LICENSE.txt",
    description="A library to compress FASTQ files using different compression techniques.",

    long_description=open("README.txt").read(),
    cmdclass={
        'build': FastQZipBuild,
        'install': FastQZipInstall,
    }
)
