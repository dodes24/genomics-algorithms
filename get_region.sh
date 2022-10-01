#!/bin/bash
# Created by: xfulop

# This script is used to get exact region from the input fasta file.
# The region is defined by the start and end position of the sequence as parameters.
# Works only with single sequence fasta files.
# Example: cat DNA.fasta | ./get_region.sh 100 200 > DNA_region.fasta

# add header to the output file
#  remove header from fasta(first line with >)
#  multiline to one line
#  get the region with user input

echo ">region $1-$2" | cat -
grep -v -e "^>" | tr -d '\n' | cut -c $1-$2

