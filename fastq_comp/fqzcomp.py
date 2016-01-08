"""It provides wrapper to Fqzcomp (http://sourceforge.net/projects/fqzcomp/)
functionalities.
"""

import os
from os import path
import subprocess
from subprocess import call, PIPE, STDOUT
import fastq_comp
try:
    from subprocess import DEVNULL
except ImportError:
    DEVNULL = open(os.devnull, 'wb')

# fqz_comp is the final utility that does the work.
FQZ_EXE = "fqz_comp"


def compress(in_file, out_file):
    """Compresses the in_file to out_file using Fqzcomp utility/algorithm.

    Args:
        in_file: Input FASTQ file that needs to be compressed.
        out_file: Compressed FASTQ file produced by the utility.
    """

    print("Performing FQZ compression on a FASTQ file")
    print("Input File: " + in_file)
    print("Output file: " + out_file)

    cmd = fastq_comp.BASE_EXE_LOC + FQZ_EXE
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
        rcode = call([cmd, in_file, out_file], stdout=DEVNULL, stderr=STDOUT)
    except subprocess.CalledProcessError as cp:
        raise Exception("Subprocess call failed. " + cp.output)
    except OSError:
        raise Exception("Subprocess call failed. The command is not found.")
    print("Return code from the process: " + str(rcode))
    print("Done. The compressed file is available at: " + out_file)


def decompress(in_file, out_file):
    """Decompresses the in_file to out_file using Fqzcomp utility/algorithm.

    Args:
        in_file: Input FASTQ file that needs to be decompressed.
        out_file: FASTQ file produced by the utility.
    """

    print("Performing FQZ compression on a FASTQ file")
    print("Input File: " + in_file)
    print("Output file: " + out_file)

    cmd = fastq_comp.BASE_EXE_LOC + FQZ_EXE
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
        rcode = call([cmd, "-d", in_file, out_file], stdout=DEVNULL, stderr=STDOUT)
    except subprocess.CalledProcessError as cp:
        raise Exception("Subprocess call failed. " + cp.output)
    except OSError:
        raise Exception("Subprocess call failed. The command is not found.")
    print("Return code from the process: " + str(rcode))
    print("Done. The uncompressed file is available at: " + out_file)


def test():
    """It is a test function to just run a shell script
    """
    cmd = fastq_comp.BASE_EXE_LOC + FQZ_EXE
    cmd_out = subprocess.check_output([cmd, "-h"])
    print(cmd_out)