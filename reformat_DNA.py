#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
přeformátujte soubor s DNA (AA) na fasta formát.
Program by měl vymazat všechny znaky mimo IUB kódů pro DNA
nebo aminokyseliny
"""

# take file with one sequence and create fasta format
# remove all characters except IUB codes for DNA or amino acids

import sys
import textwrap


def make_fasta_from_dna():
    # wrap sequence to 60 characters per line
    wrapper = textwrap.TextWrapper(width=60)

    # open file for reading
    file_in = input("Enter file name: ")
    file_out = input("Enter output file name: ")
    with open(file_in, mode="r") as file_in:
        # open file for writing and create fasta format
        file_out = open(file_out, "w")
        read_data = file_in.read()
        # remove all characters except IUB codes for DNA or amino acids
        sequence = ""
        for x in read_data:
            if x in "ACDEFGHIKLMNPQRSTVWYatgc":
                sequence = sequence + x
                sequence_60 = wrapper.fill(text=sequence)
                fasta_data = f'> seq \n{sequence_60}'
        # write data to file
        file_out.write(fasta_data)


# if there is standard input then use it asi input file and standard output as output file
if len(sys.argv) == 1: # if there is no input file
    make_fasta_from_dna()

else:
    # if there is no standard input then use user input file and user output file
    make_fasta_from_dna()  # if there is input file

