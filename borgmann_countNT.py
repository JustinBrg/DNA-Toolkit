#!/usr/bin/python3
import sys

dna = open(sys.argv[1])
nucs = (sys.argv[2])        #ACGT

nucleotides = {
                    "A": 0, "C": 0, "G": 0, "T": 0
                }

fasta_header = dna.readline().rstrip()#no new line


dna = dna.read()   #read() so i can iterate through the file

'#for each position of dna checking if it is a nuc of nucs'
for nuc in dna:
    for nc in nucs:
        if nuc == nc:
            nucleotides[nuc] += 1


'#printing header out [1:} so ">" is cut out'
print(fasta_header[1:], nucleotides["A"], nucleotides["C"], nucleotides["G"], nucleotides["T"])
