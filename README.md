# Introduction

This library provides a set of functions to compress FASTQ files based on some pre-existing applications listed below.

# 1. Fqzcomp 
This library is available at http://sourceforge.net/projects/fqzcomp/.

Usage of this library to compress a FASTQ file using 'fqzcomp' tool as follows:

<code>from fastq_comp import fqzcomp</code>

<code>input_fastq_file = "human_sample_1.fastq"</code>

<code>output_compressed_fq_file = "comp_human_sam_1.qz"</code>

<code>fqzcomp.compress(input_fastq_file, output_compressed_fq_file)</code>