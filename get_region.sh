#!/bin/bash

#  remove header from fasta(first line with >)
#  multiline to one line
#  get the region with user input
grep -v -e "^>" | tr -d '\n' | cut -c $1-$2
