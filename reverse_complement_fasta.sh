#!/bin/bash
# Created by: xfulop


# This script is used to get reverse complement of a sequence from fasta file
# Example: cat DNA.fasta | ./reverse_complement_fasta.sh > file_reverse.fasta

tr 'ACGTacgt' 'TGCAtgca' | rev
