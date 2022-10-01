#!/bin/bash
# Created by: xfulop

# This script is used to reformat DNA or AA sequences and create a fasta file.
# Example: cat file.txt | ./reformat.sh > file.fasta
#          cat file.txt | ./reformat.sh -a | ./statistic_DNA.sh

if [ $# -ne 1 ]; then
    echo $"> SEQ"
    grep -oz '[A-N,P-T,V-Z,a-n,p-t,v-z,*,-]*' $1 | tr -d "\r" | tr -d "\n" | tr -d " " | tr -d '\000'
else
    echo $">$1"
    grep -oz '[A-N,P-T,V-Z,a-n,p-t,v-z,*,-]*' $1 | tr -d "\r" | tr -d "\n" | tr -d " " | tr -d '\000'
fi

