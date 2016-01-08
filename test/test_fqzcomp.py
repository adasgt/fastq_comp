import os
import unittest
import fastq_comp
from fastq_comp import fqzcomp

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


class FQZCompTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_dir = DATA_DIR
        cls.fastq = DATA_DIR + "/sample.fastq"
        cls.exc = fastq_comp.BASE_EXE_LOC + fqzcomp.FQZ_EXE
        if not os.path.isfile(cls.exc):
            raise fastq_comp.FASTQCompError("Run './setup.py build' before running the test.")
        if not os.path.isfile(cls.fastq):
            raise fastq_comp.FASTQCompError("No FASTQ file is found in 'data' directory.")

    def test_compress(self):
        try:
            fqzcomp.compress(self.fastq, self.data_dir + "/compressed-sample.gz")
        except Exception:
            assert False

        assert True

    def test_uncompress(self):
        try:
            fqzcomp.decompress(self.data_dir + "/compressed-sample.gz", self.data_dir + "/uncompressed-sample.fastq")
        except Exception:
            assert False

        assert True

if __name__ == '__main__':
    unittest.main()

