from structures import *

print(f"5' {rndDNAseq} 3'")
print(f"   {''.join(['|' for i in range(len(rndDNAseq))])}")
print(f"3' {reverseComplement(rndDNAseq)} 5'")
