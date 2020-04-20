Fastq-Filtering With Trimming Function
Arguments input from command line.
Programs require: Python3 with basic packages argparse and statistics 
(I use Python 3.7.3, but early version could also be proper)

Usage:
python path_to_program/Parse_fastq.py [options] file_name.fastq

options:
	--min_length <integer >0>  :minimal length of sequence
	--gc_bounds <integer1 >0, <100 > (opt <integer2, >integer1, <100>) : [1] low and [2] upper bounds of GC content
	--keep_filtered :write sequences don`t pass any filter into base_name_badd_reads.fastq file
	--ouput_base_name <string> :common start of output_names, if default=file_name
	--HEADCROP <integer >0> : number of nucleotides cutting from start of sequence
	--LEADING <integer >0> :low value of quality (just decode from ascii), 
                          if quality of leading nucleotide(s) less these value, they are cut
	--TRALING <integer >0> :low value of quality (just decode from ascii),
                          if quality of trailing nucleotide(s) less these value, they are cut
	--sliding_window <integer1, >0 > <integer2, >0 > :integer1 - window size, integer2 - low value of quality, 
							if average quality of nucleotides from the end of sequence in window less then integer2
							all nucleotides from window would be cut and window slice to new end
	--CROP <integer, >0, >min_length (if required)> : maximum size of sequence we write, if it less then length of sequences, 
							cutting nucleotides from the end to CROP length

	positional argument file_name.fastq - fastq file for filtering

Trimming is carried out in the following sequence:
	1. HEADCROP
	2. LEADING
	3. TRAILING
	4. sliding_window
	5. CROP

!!! gc_bounds and min_length filters applied after trimming.

As result produce one (or two, if keep_filtered required) fastq files,
                  one with reads passed all filters (and trimmed if require), 
									second (optional) with reads which don`t passed one of filters
