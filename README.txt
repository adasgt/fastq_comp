This library provides a set of functions to compress FASTQ files based on some pre-existing applications listed below.

1. Fqzcomp: http://sourceforge.net/projects/fqzcomp/
=====================================================
1.1. Usage of this library to compress a FASTQ file using 'fqzcomp' tool as follows:

        from fastq_comp import fqzcomp

        input_fastq_file = "human_sample_1.fastq"

        output_compressed_fq_file = "comp_human_sam_1.qz"

        fqzcomp.compress(input_fastq_file, output_compressed_fq_file)
