import sys

dna_string = open(sys.argv[1])
dna_string = dna_string.read()

complement = []
for nuc in dna_string:
    if nuc == 'A':
        complement.append('T')
    elif nuc == 'G':
        complement.append('C')
    elif nuc == 'T':
        complement.append('A')
    else:
        complement.append('G')

string = "".join([n.strip() for n in complement])
print(" DNA                : 5' -> " + dna_string + " 3'")
print(f"                            { ''.join(['|' for c in range(len(dna_string))])} ")
print(" Reverse COMPLEMENT : 5' -> " + string[::-1] + " 3'")
