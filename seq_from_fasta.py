#!/usr/bin/env python
# encoding=utf-8

"""
This script is used to read a sequence from fasta file.
"""

import sys
import textwrap

wrapper = textwrap.TextWrapper(width=70)

with open(sys.argv[1], 'r') as f: #  read fasta file from argument
    for line in f: #  read line by line
        if line.startswith('>'):
            header = line.strip()
        else:
            sequence = line.strip()
            sequence = wrapper.fill(text=sequence)
            print(f'{header}', f'{sequence}', sep='\n')



