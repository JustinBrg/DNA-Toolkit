#!/usr/bin/env python3
# Sylvie Baier

import sys

# Nucleotide Frequencies

# read command line arguments

genome_path = sys.argv[1]
genome_sequence = ''
with open(genome_path, 'r') as file:
    for line in file:
        if not line.startswith('>'):
            genome_sequence += line.rstrip()
        else:
            header = line.rstrip().split('>')[1]

counting_letters = sys.argv[2]

counting_letters_dic = {}
for element in counting_letters:
    counting_letters_dic[element] = 0


def count_letters(sequence, dictionary):
    d = dictionary  # dictionary with letters and its frequencies

    for letter in sequence:
        if letter in d:
            d[letter] += 1
    return d


result_dictionary = count_letters(genome_sequence, counting_letters_dic)
letters = []
for element in sorted(result_dictionary.keys()):
    letters.append(element)

frequencies = []
for value in letters:
    frequencies.append((result_dictionary[value]))

result = [header, *frequencies]
print(*result, sep='\t')
