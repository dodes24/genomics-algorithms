#!/usr/bin/env python
# encoding=utf-8

"""
This script is used to read a sequence from fasta file.
"""

import sys
import textwrap

wrapper = textwrap.TextWrapper(width=70)

with open(sys.argv[1], 'r') as f:  # read fasta file from argument
    for line in f:  # read line by line
        if line.startswith('>'):  # if line starts with > then it is header
            header = line.strip()  # strip line from whitespaces
        else:  # if line is not header then it is sequence
            sequence = line.strip()  # strip line from whitespaces
            sequence = wrapper.fill(text=sequence)  # wrap sequence to 70 characters
            print(f'{header}', f'{sequence}', sep='\n')  # print header and sequence

