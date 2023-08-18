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

# >NM_000207.3 Homo sapiens insulin (INS), transcript variant 1, mRNA
NM_000207_3 = "AGCCCTCCAGGACAGGCTGCATCAGAAGAGGCCATCAAGCAGATCACTGTCCTTCTGCCATGGCCCTGTGGATGCGCCTCCTGCCCCTGCTGGCGCTGCTGGCCCTCTGGGGACCTGACCCAGCCGCAGCCTTTGTGAACCAACACCTGTGCGGCTCACACCTGGTGGAAGCTCTCTACCTAGTGTGCGGGGAACGAGGCTTCTTCTACACACCCAAGACCCGCCGGGAGGCAGAGGACCTGCAGGTGGGGCAGGTGGAGCTGGGCGGGGGCCCTGGTGCAGGCAGCCTGCAGCCCTTGGCCCTGGAGGGGTCCCTGCAGAAGCGTGGCATTGTGGAACAATGCTGTACCAGCATCTGCTCCCTCTACCAGCTGGAGAACTACTGCAACTAGACGCAGCCCGCAGGCAGCCCCACACCCGCCGCCTCCTGCACCGAGAGAGATGGAATAAAGCCCTTGAACCAGC"

print(f'Reading frames: ')
for frame in readingFrames(NM_000207_3):
    print(frame)

print(f'\nProtein Sequence: {proteins(frame)}')

print(f'All proteins in 6 open reading frames: ')
for protein in all_proteins(NM_000207_3, 0, 0, True):
    print(f'{protein}')
