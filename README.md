# Python_BI_2022
Repo for homeworks from the Python course, Bioinformatics Institute 2022.

> *by* Anna Chechenina  <br />
> chechenina.anna@yahoo.com

## Homework 1 (collections)

The program called "nucleic_acids.py" is written without using any side-libraries. It takes and executes commands recursively. You can find list of commands with the description below:

* *exit* — end of the program execution
* *transcribe* — takes DNA sequence as input and prints the corresponding RNA secuence
* *reverse* — takes DNA/RNA sequence as input and prints the reverted sequence
* *complement* — takes DNA/RNA sequence as input and prints the complemenraty sequence to the given one
* *reverse complement* — takes DNA/RNA sequence as input and prints the reverted complement sequence
* *translate* — takes DNA/RNA sequence as input and print the protein sequence of the first reading frame inside the sequence
* *first orf (also callable as "first ORF")* — takes DNA/RNA sequence as input and prints the first found open reading frame (if there are no stop codons it prints the sequence starting from start codon till the end of the sequence)

## Homework 2 (files and functions)

The program called "fastq_filtrator.py" is written without using any side-libraries. The program can be used to filter fastq files with given parameters like length, GC-content and a quality of each read. An output of the program is a fastq file with all reads that satisfy given instructions. It contains the main function with the following arguments:

* *input_fastq* — path to fastq file to filter
* *output_file_prefix* — prefix of the output file, the file with satisfactory reads will have a "_passed.fastq" index and the file with unsatisfactory reads will have "_failed.fastq" index (only if save_filtered = True)
* *gc_bounds* — tuple of two values, the GC-content limits for each read as a percentage (default (0, 100), so all reads will pass the test). If the tuple contains only one number it will be used as an upper boundary. Examples: gc_bounds = (20, 80), only reads with GC-content between 20% and 80% will be saved; gc_bounds = 44.4 — reads with GC-content less than 44.4% will be saved.
* *length_bounds* — tuple of two values, length limits for each read (0, 2**32) on default.
* *quality_threshold* — threshold for the average mean quality for each read, the decoding of the fastq quality marks is done according to phred33 scale (default quality_threshold = 0)
* *save_filtered* — if True, additional file with filtered out reads will be returned (default save_filtered = False)

## Homework 3 (environments)

This repo conteins ultraviolence.py script and the requirements file to run this script. 
You can find the instructions in the HW3 repo under the corresponding brunch.

