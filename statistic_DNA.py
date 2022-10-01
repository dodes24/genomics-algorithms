#!/usr/bin/env python
# encoding=utf-8
# Created by: xfulop
"""
basic fasta file statistics (sequence length, ACGT composition, ambiguous bases, checksum)
(output from reformat_DNA and compare with mm_pax6.fasta)
"""
from collections import Counter
import sys
import binascii
import textwrap
import argparse

sequence = ''
wrapper = textwrap.TextWrapper(width=70)

parser = argparse.ArgumentParser(description='This script is used to print some basic statistics about sequence .\
                                            It can be used just with stdin and you have to redirect output to a file.\
                                            Example: cat dna.fasta | ./statistic_DNA.py > statistics.txt')

args = parser.parse_args()


for line in sys.stdin:
    if line.startswith('>'):
        header = line.strip()
    else:
        sequence = sequence + line.strip()


sequence_length = len(sequence)
acgtn_collection = Counter(sequence.upper())
checksum = (str(hex(binascii.crc32(sequence.upper().encode('utf-8')))))

# print just statistics results
print(str(header))
print("Sequence length: " + str(sequence_length))
print("A content: " + str(float(round(acgtn_collection["A"]/sequence_length, 2))))
print("C content: " + str(float(round(acgtn_collection["C"]/sequence_length, 2))))
print("G content: " + str(float(round(acgtn_collection["G"]/sequence_length, 2))))
print("T content: " + str(float(round(acgtn_collection["T"]/sequence_length, 2))))
print("N content: " + str(float(round(acgtn_collection["N"]/sequence_length, 2))))
print("GC content: " + str(float(round((acgtn_collection["G"]+acgtn_collection["C"])/sequence_length, 2))))
print("ACGT composition: " + str(acgtn_collection))
print("ambiguous bases: " + str(acgtn_collection["N"]))
print("checksum: " + str(checksum))
# if there will be output sequence in fasta format
sequence = wrapper.fill(text=sequence)

