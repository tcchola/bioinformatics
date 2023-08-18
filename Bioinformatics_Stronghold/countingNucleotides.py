import collections
from structures import *

DNAString = validateSequence(rndDNAseq)

print(f"5' {DNAString} 3'")
print(f'Sequence Length: {len(DNAString)}')
print(f'Nucleotide Frequency: {countNucleotides(DNAString)}')
