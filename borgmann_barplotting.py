#!/usr/bin/python3
import sys
import matplotlib.pyplot as plt
import numpy as np

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

# adapted from https://matplotlib.org/3.1.1/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
labels = [fasta_header[1:]]#name of genome we get the distribution for
a_nuc = [nucleotides["A"]]
c_nuc = [nucleotides["C"]]
g_nuc = [nucleotides["G"]]
t_nuc = [nucleotides["T"]]
x = np.arange(len(labels))  # the label locations
width = 0.4  # the width of the bars
fig, ax = plt.subplots()
rects1 = ax.bar(x + (width - width/2), a_nuc, width, label=nucs[0])  #A       #width/2 usable for every size of width
rects2 = ax.bar(x + (width + width/2), c_nuc, width, label=nucs[1]) #C
rects3 = ax.bar(x - (width + width/2), g_nuc, width, label=nucs[2])  #G
rects4 = ax.bar(x - (width - width/2), t_nuc, width, label=nucs[3])  #T

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Amount')
ax.set_title('Nucleotides distribution per genome')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

fig.tight_layout()

plt.show()
