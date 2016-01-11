# Introduction

This library provides a set of functions to compress FASTQ files based on some pre-existing applications listed below.

**1. Fqzcomp:** 
This library is available at http://sourceforge.net/projects/fqzcomp/. 

# How to use this library?

Clone the git repository

<code>git clone https://github.com/adasgt/fastq_comp.git</code>

Change directory to the git repository i.e. "fastq_comp"

<code>git clone https://github.com/adasgt/fastq_comp.git</code>

Change directory to the git repository i.e. "fastq_comp"

<code>cd fastq_comp</code>

Run make

<code>make</code>

Run setup.py to make the package distribution

<code>python setup.py sdist</code>

Install the library

<code>pip install --user dist/fastq_comp-0.0.1.tar.gz</code>


**Usage of this library in python source to compress a FASTQ file:**

<code>from fastq_comp import fqzcomp</code>

<code>input_fastq_file = "human_sample_1.fastq"</code>

<code>output_compressed_fq_file = "comp_human_sam_1.qz"</code>

<code>fqzcomp.compress(input_fastq_file, output_compressed_fq_file)</code>