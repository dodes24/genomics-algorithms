#!/usr/bin/env python
# encoding=utf-8
# Created by: xfulop
"""
This script is used to translate DNA sequence into protein sequence.
"""
import argparse
import sys
import textwrap

parser = argparse.ArgumentParser(description='This script is used to translate DNA sequence into protein sequence.\
                                              It can be used just with stdin and you have to redirect output to a file.\
                                              This script translates with standard genetic code, and you will get\
                                              all 6 ORFs (3 forward and 3 reverse).\
                                              Usually is selected Standard genetic code.\
                                              If you want to choose different genetic code please rewrite variable\
                                              SELECTED_GENETIC_CODE to desired genetic code .\
                                              Example: cat dna.fasta | ./translate.py > protein.fasta')
args = parser.parse_args()

wrapper = textwrap.TextWrapper(width=70)


def main():
    """
    This is main function
    """
    ORFTranslationPrinted()

############################################################################################################
# SELECT GENETIC CODE FOR TRANSLATION FROM THESE OPTIONS:
"""    
    Standard_Code
    Vertebrate_Mitochondrial_Code
    Yeast_Mitochondrial_Code
    Mold_Protozoan_Coelenterate_Mitochondrial_and_Mycoplasma_Spiroplasma_Code
    Invertebrate_Mitochondrial_Code
    Ciliate_Dasycladacean_and_Hexamita_Nuclear_Code
    Echinoderm_and_Flatworm_Mitochondrial_Code
    Euplotid_Nuclear_Code
    Bacterial_Archaeal_and_Plant_Plastid_Code
    Alternative_Yeast_Nuclear_Code
    Ascidian_Mitochondrial_Code
    Alternative_Flatworm_Mitochondrial_Code
    Blepharisma_Nuclear_Code
    Chlorophycean_Mitochondrial_Code
    Trematode_Mitochondrial_Code
    Scenedesmus_obliquus_mitochondrial_Code
    Thraustochytrium_Mitochondrial_Code
    Pterobranchia_mitochondrial_code
    Candidate_Division_SR1_and_Gracilibacteria_Code
"""
Base1 = "UUUUUUUUUUUUUUUUCCCCCCCCCCCCCCCCAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGG"
Base2 = "UUUUCCCCAAAAGGGGUUUUCCCCAAAAGGGGUUUUCCCCAAAAGGGGUUUUCCCCAAAAGGGG"
Base3 = "UCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAGUCAG"

Standard_Code = \
    "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
Vertebrate_Mitochondrial_Code = \
    "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSS**VVVVAAAADDEEGGGG"
Yeast_Mitochondrial_Code = \
    "FFLLSSSSYY**CCWWTTTTPPPPHHQQRRRRIIMMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
Mold_Protozoan_Coelenterate_Mitochondrial_and_Mycoplasma_Spiroplasma_Code = \
    "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
Invertebrate_Mitochondrial_Code = \
    "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSSSSVVVVAAAADDEEGGGG"
Ciliate_Dasycladacean_and_Hexamita_Nuclear_Code = \
    "FFLLSSSSYYQQCC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
Echinoderm_and_Flatworm_Mitochondrial_Code = \
    "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIIMTTTTNNNKSSSSVVVVAAAADDEEGGGG"
Euplotid_Nuclear_Code = \
    "FFLLSSSSYY**CCCWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
Bacterial_Archaeal_and_Plant_Plastid_Code = \
    "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
Alternative_Yeast_Nuclear_Code = \
    "FFLLSSSSYY**CC*WLLLSPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
Ascidian_Mitochondrial_Code = \
    "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNKKSSGGVVVVAAAADDEEGGGG"
Alternative_Flatworm_Mitochondrial_Code = \
    "FFLLSSSSYYY*CCWWLLLLPPPPHHQQRRRRIIIMTTTTNNNKSSSSVVVVAAAADDEEGGGG"
Blepharisma_Nuclear_Code = \
    "FFLLSSSSYY*QCC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
Chlorophycean_Mitochondrial_Code = \
    "FFLLSSSSYY*LCC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
Trematode_Mitochondrial_Code = \
    "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIMMTTTTNNNKSSSSVVVVAAAADDEEGGGG"
Scenedesmus_obliquus_mitochondrial_Code = \
    "FFLLSS*SYY*LCC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
Thraustochytrium_Mitochondrial_Code = \
    "FF*LSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
Pterobranchia_mitochondrial_code = \
    "FFLLSSSSYY**CCWWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSSKVVVVAAAADDEEGGGG"
Candidate_Division_SR1_and_Gracilibacteria_Code = \
    "FFLLSSSSYY**CCGWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"

SELECTED_GENETIC_CODE = Vertebrate_Mitochondrial_Code


###########################################################################################################


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


def createGeneticCodeDict(SELECTED_GENETIC_CODE):
    """
    This function creates a dictionary that contains our genetic code.
    """
    genetic_code = {}
    for i in range(0, 64):
        codon = Base1[i] + Base2[i] + Base3[i]
        amino_acid = SELECTED_GENETIC_CODE[i]
        genetic_code[codon] = amino_acid
    return genetic_code


'''
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

The_Vertebrate_Mitochondrial_Code = {
    'AAA': 'K', 'CAA': 'Q', 'GAA': 'E', 'UAA': '*',
    'AAC': 'N', 'CAC': 'H', 'GAC': 'D', 'UAC': 'Y',
    'AAG': 'K', 'CAG': 'Q', 'GAG': 'E', 'UAG': '*',
    'AAU': 'N', 'CAU': 'H', 'GAU': 'D', 'UAU': 'Y',
    'ACA': 'T', 'CCA': 'P', 'GCA': 'A', 'UCA': 'S',
    'ACC': 'T', 'CCC': 'P', 'GCC': 'A', 'UCC': 'S',
    'ACG': 'T', 'CCG': 'P', 'GCG': 'A', 'UCG': 'S',
    'ACU': 'T', 'CCU': 'P', 'GCU': 'A', 'UCU': 'S',
    'AGA': '*', 'CGA': 'R', 'GGA': 'G', 'UGA': 'W',
    'AGC': 'S', 'CGC': 'R', 'GGC': 'G', 'UGC': 'C',
    'AGG': '*', 'CGG': 'R', 'GGG': 'G', 'UGG': 'W',
    'AGU': 'S', 'CGU': 'R', 'GGU': 'G', 'UGU': 'C',
    'AUA': 'M', 'CUA': 'L', 'GUA': 'V', 'UUA': 'L',
    'AUC': 'I', 'CUC': 'L', 'GUC': 'V', 'UUC': 'F',
    'AUG': 'M', 'CUG': 'L', 'GUG': 'V', 'UUG': 'L',
    'AUU': 'I', 'CUU': 'L', 'GUU': 'V', 'UUU': 'F', }

'''


# unit test for two dictionaries above


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
            print(wrapper.fill(proteinTranslation(seq[frame - 1:], createGeneticCodeDict(SELECTED_GENETIC_CODE))))
            print(head, 'Reverse complement: ORF -%d' % frame)
            print(wrapper.fill(proteinTranslation(reverseComplement(seq)[frame - 1:],
                                                  createGeneticCodeDict(SELECTED_GENETIC_CODE))))


if __name__ == '__main__':
    main()
