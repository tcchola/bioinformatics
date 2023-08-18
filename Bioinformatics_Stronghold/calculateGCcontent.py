from structures import *


def readFile(filepath):
    """Read a file"""
    with open(filepath, 'r') as f:
        return [l.strip() for l in f.readlines()]


FASTA_File = readFile("test_data/gc_content.txt")
FASTA_Dictionary = {}
FASTA_Label = ""

for line in FASTA_File:
    if '>' in line:
        FASTA_Label = line
        FASTA_Dictionary[FASTA_Label] = ""
    else:
        FASTA_Dictionary[FASTA_Label] += line

print(FASTA_Dictionary)

Result_Dictionary = {key: calculateGC(value)
                     for (key, value) in FASTA_Dictionary.items()}

print(Result_Dictionary)

maxGCkey = max(Result_Dictionary, key=Result_Dictionary.get)

print(f'{maxGCkey}\n{Result_Dictionary}[maxGCkey]')
