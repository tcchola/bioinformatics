from structures import *
from main import *

print(f'All proteins in 6 open reading frames: ')
for protein in all_proteins(NM_000207_3, 0, 0, True):
    print(f'{protein}')
