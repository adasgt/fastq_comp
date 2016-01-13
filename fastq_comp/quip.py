"""This module provides FASTQ compression and decompression using the
QUIP utility. Details about this utility can be found at
https://github.com/dcjones/quip.
"""
import os
from os import path
import subprocess
from subprocess import call, STDOUT
from distutils import spawn
import fastq_comp

# QUIP utility name
QUIP_EXE = "quip"
# find full path of the QUIP_EXE
QUIP_CMD = spawn.find_executable(QUIP_EXE)
# if QUIP_CMD is None or blank, print error message and raise an exception
if QUIP_CMD is None:
    print(QUIP_EXE + " is not found in the system.")
    exit(1)

DEVNULL = open(os.devnull, 'wb')


def compress(in_file):
    """Compresses the in_file to out_file using QUIP utility/algorithm.

    Args:
        in_file: Input FASTQ file that needs to be compressed.
        The utility produces an output file with same name as the input file but
        with a .qp extension.
    """

    print("Performing QUIP compression on a FASTQ file")

    # check that the in_file exists
    if not os.path.isfile(in_file):
        raise Exception("Input FASTQ file does not exist.")
    # Check that the parent directory of the out_file exists
    # Get the parent directory
    pdir = "."
    if '/' in in_file:
        pdir = path.dirname(in_file)
    try:
        rcode = call([QUIP_CMD, in_file], stdout=DEVNULL, stderr=STDOUT)
    except subprocess.CalledProcessError as cp:
        raise Exception("Subprocess call failed. " + cp.output)
    except OSError:
        raise Exception("Subprocess call failed. The command is not found.")

    print("Done. The compressed file is available at: " + in_file + ".qp")


def decompress(in_file):
    """Decompresses the in_file to out_file using QUIP utility/algorithm.

    Args:
        in_file: Input FASTQ file that needs to be decompressed. A compressed quip file has .qp
        extension.
    """

    print("Performing QUIP decompression on a compressed FASTQ file")

    # check that the in_file exists
    if not os.path.isfile(in_file):
        raise Exception("Input compressed file does not exist.")
    # Check that the parent directory of the out_file exists
    # Get the parent directory
    try:
        rcode = call([QUIP_CMD, in_file,"-d", "-f"], stdout=DEVNULL, stderr=STDOUT)
    except subprocess.CalledProcessError as cp:
        raise Exception("Subprocess call failed. " + cp.output)
    except OSError:
        raise Exception("Subprocess call failed. The command is not found.")

    print("Done.")
