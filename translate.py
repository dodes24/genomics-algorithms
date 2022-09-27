#!/usr/bin/env python
# encoding=utf-8

"""
This script is used to translate DNA sequence into protein sequence.
"""
import sys
import textwrap

wrapper = textwrap.TextWrapper(width=70)


def main():
    """
    This is main function
    """
    ORFTranslationPrinted()


def readFastaFile():
    """
    This function reads a fasta file and returns header and sequences:
    """
    sequences = []
    headers = []
    seq = ''
    for line in sys.stdin:
        if line.startswith('>'):
            head = line.strip()
            headers.append(head)
            if seq:
                sequences.append(seq)
            seq = ''
        else:
            seq += line.rstrip()
    if seq:
        sequences.append(seq)
    return headers, sequences


read_fasta = readFastaFile()

#  firstly we define a dictionary that contains our genetic code. Here we use strings containing
#  three nucleotide letters as the dictionary keys; these are the codons. The value associated with
#  each codon is thee-letter code of the appropriate amino acid or the None object if it is a
#  stop codon.

STANDARD_GENETIC_CODE = {
    'AAA': 'K', 'CAA': 'Q', 'GAA': 'E', 'UAA': '*',
    'AAC': 'N', 'CAC': 'H', 'GAC': 'D', 'UAC': 'Y',
    'AAG': 'K', 'CAG': 'Q', 'GAG': 'E', 'UAG': '*',
    'AAU': 'N', 'CAU': 'H', 'GAU': 'D', 'UAU': 'Y',
    'ACA': 'T', 'CCA': 'P', 'GCA': 'A', 'UCA': 'S',
    'ACC': 'T', 'CCC': 'P', 'GCC': 'A', 'UCC': 'S',
    'ACG': 'T', 'CCG': 'P', 'GCG': 'A', 'UCG': 'S',
    'ACU': 'T', 'CCU': 'P', 'GCU': 'A', 'UCU': 'S',
    'AGA': 'R', 'CGA': 'R', 'GGA': 'G', 'UGA': '*',
    'AGC': 'S', 'CGC': 'R', 'GGC': 'G', 'UGC': 'C',
    'AGG': 'R', 'CGG': 'R', 'GGG': 'G', 'UGG': 'W',
    'AGU': 'S', 'CGU': 'R', 'GGU': 'G', 'UGU': 'C',
    'AUA': 'I', 'CUA': 'L', 'GUA': 'V', 'UUA': 'L',
    'AUC': 'I', 'CUC': 'L', 'GUC': 'V', 'UUC': 'F',
    'AUG': 'M', 'CUG': 'L', 'GUG': 'V', 'UUG': 'L',
    'AUU': 'I', 'CUU': 'L', 'GUU': 'V', 'UUU': 'F', }


def reverseComplement(rev_seq):
    """
    This function returns reverse complement of a DNA sequence
    """
    seq = rev_seq.replace('T', 'U')  # Make sure we have RNA sequence
    complement = {'A': 'U', 'C': 'G', 'G': 'C', 'U': 'A'}
    seq = ''.join(complement.get(base, base) for base in reversed(seq))
    return seq


def proteinTranslation(seq, genetic_code):
    """
    This function translates a nucleic acid sequence into a protein sequence
    """
    seq = seq.replace('T', 'U')  # Make sure we have RNA sequence
    protein_seq = []

    i = 0
    while i + 2 < len(seq):
        codon = seq[i:i + 3]
        amino_acid = genetic_code[codon]
        # if amino_acid == '*':  # Found stop codon
        #    break
        protein_seq.append(amino_acid)
        i += 3
    return ''.join(protein_seq)


def ORFTranslationPrinted():
    """
    This function prints protein translation of all six reading frames
    """

    for head, seq in zip(read_fasta[0], read_fasta[1]):
        for frame in range(1, 4):
            print(head, 'Reading frame %d:' % frame)
            print(wrapper.fill(proteinTranslation(seq[frame - 1:], STANDARD_GENETIC_CODE)))
            print(head, 'Reverse complement: ORF -%d' % frame)
            print(wrapper.fill(proteinTranslation(reverseComplement(seq)[frame - 1:], STANDARD_GENETIC_CODE)))


if __name__ == '__main__':
    main()

#  ToDo: 1. Add a function to choose between standard and alternative genetic code