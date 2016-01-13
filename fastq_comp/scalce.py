"""This module provides FASTQ compression and decompression using the
SCALCE utility. Details about this utility can be found at
http://sfu-compbio.github.io/scalce/.
"""
import os
from os import path
import subprocess
from subprocess import call, STDOUT
from distutils import spawn
import fastq_comp

# scalce utility name
SCALCE_EXE = "scalce"
# find full path of the SCALCE_EXE
SCALCE_CMD = spawn.find_executable(SCALCE_EXE)
# if SCALCE_CMD is None or blank, print error message and raise an exception
if SCALCE_CMD is None:
    print(SCALCE_EXE + " is not found in the system.")
    exit(1)

DEVNULL = open(os.devnull, 'wb')


def compress(in_file, out_file):
    """Compresses the in_file to out_file using SCALCE utility/algorithm.

    Args:
        in_file: Input FASTQ file that needs to be compressed.
        out_file: Compressed FASTQ file produced by the utility.
    """

    print("Performing SCALCE compression on a FASTQ file")

    # check that the in_file exists
    if not os.path.isfile(in_file):
        raise Exception("Input FASTQ file does not exist.")
    # Check that the parent directory of the out_file exists
    # Get the parent directory
    pdir = "."
    if '/' in out_file:
        pdir = path.dirname(out_file)
    # check if pdir exists
    if not os.path.exists(pdir):
        raise fastq_comp.FASTQCompError("Output directory does not exist.")
    try:
        rcode = call([SCALCE_CMD, in_file, '-o', out_file, '-B', '2G'], stdout=DEVNULL, stderr=STDOUT)
    except subprocess.CalledProcessError as cp:
        raise Exception("Subprocess call failed. " + cp.output)
    except OSError:
        raise Exception("Subprocess call failed. The command is not found.")

    print("Done. The compressed files(.scalcen, .scalcer and .scalceq) are available at: " + pdir)


def decompress(in_file, out_file):
    """Decompresses the in_file to out_file using SCALCE utility/algorithm.

    Args:
        in_file: Input FASTQ file that needs to be decompressed.
        out_file: FASTQ file produced by the utility.
    """

    print("Performing SCALCE decompression on a compressed FASTQ file")

    # check that the in_file exists
    if not os.path.isfile(in_file):
        raise Exception("Input FASTQ file does not exist.")
    # Check that the parent directory of the out_file exists
    # Get the parent directory
    pdir = "."
    if '/' in out_file:
        pdir = path.dirname(out_file)
    # check if pdir exists
    if not os.path.exists(pdir):
        raise fastq_comp.FASTQCompError("Output directory does not exist.")
    try:
        rcode = call([SCALCE_CMD, in_file,"-d", "-o", out_file], stdout=DEVNULL, stderr=STDOUT)
    except subprocess.CalledProcessError as cp:
        raise Exception("Subprocess call failed. " + cp.output)
    except OSError:
        raise Exception("Subprocess call failed. The command is not found.")

    print("Done. The decompressed file is available at: " + out_file)
