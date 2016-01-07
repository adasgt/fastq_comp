from __future__ import absolute_import, division, print_function, unicode_literals
import os
from os import path
import subprocess
from subprocess import call, PIPE, STDOUT
try:
    from subprocess import DEVNULL
except ImportError:
    DEVNULL = open(os.devnull, 'wb')

# Base location of all the third party executables or libraries for compression of the FASTQ
BASE_EXE_LOC = os.path.dirname(os.path.abspath(__file__)) + "/static/"
# fqz_comp is a compression tool that will compress and decompress the FASTQ files.
# Refer to Fqzcomp's web site i.e. http://sourceforge.net/projects/fqzcomp/ for details.
FQZ_EXE = "fqz_comp"


def fqz_compress(in_file, out_file):
    """Compresses the input file using Fqzcomp algorithm.

    Args:
        in_file: Input FASTQ file that needs to be compressed.
        out_file: Compressed FASTQ file
    """
    
    print("Performing FQZ compression on a FASTQ file")
    print("Input File: " + in_file)
    print("Output file: " + out_file)

    cmd = BASE_EXE_LOC + FQZ_EXE
    # check that the in_file exists
    if not os.path.isfile(in_file):
        raise Exception("Input file does not exist.")
    # Check that the parent directory of the out_file exists
    # Get the parent directory
    pdir = "."
    if '/' in out_file:
        pdir = path.dirname(out_file)
    # check if pdir exists
    if not os.path.exists(pdir):
        raise Exception("Output directory does not exist.")
    try:
        rcode = call([cmd, in_file, out_file], stdout=DEVNULL, stderr=STDOUT)
    except subprocess.CalledProcessError as cp:
        raise Exception("Subprocess call failed. " + cp.message)
    except OSError:
        raise Exception("Subprocess call failed. The command is not found.")
    print("Done. The compressed file is available at: " + out_file)

def test():
    """It is a test function to just run a shell script
    """
    cmd = BASE_EXE_LOC + FQZ_EXE
    cmd_out = subprocess.check_output([cmd, "-h"])
    print(cmd_out)