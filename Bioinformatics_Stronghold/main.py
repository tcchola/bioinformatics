### ALL OPERATIONS IN ONE FILE ###

from structures import *

print(f"5' {validateSequence(rndDNAseq)} 3'")
print(f"   {''.join(['|' for i in range(len(rndDNAseq))])}")
print(f"3' {reverseComplement(rndDNAseq)} 5'\n")

print(f'Sequence Length: {len(validateSequence(rndDNAseq))}')
print(f'Nucleotide Frequency: {countNucleotides(validateSequence(rndDNAseq))}')
print(f"RNA: {transcribe(rndDNAseq)}")
print(f"GC: {calculateGC(rndDNAseq)}%")
print(f'Codons: {translate(rndDNAseq, 0)}')
print(f'Codon Frequency of L: {codonFrequency(rndDNAseq, "L")}\n')
