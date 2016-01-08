from __future__ import absolute_import, division, print_function, unicode_literals
import os

# Base location of the fqzcomp executable for compression and decompression of the FASTQ file
BASE_EXE_LOC = os.path.dirname(os.path.abspath(__file__)) + "/static/"


class FASTQCompError(Exception):
    """Custom exception for fastq_comp library.
    """
    def __init__(self, *message, **code):
        Exception.__init__(self, *message, **code)
