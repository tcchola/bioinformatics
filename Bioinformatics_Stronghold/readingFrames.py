from structures import *
from main import *

print(f'Reading frames: ')
for frame in readingFrames(NM_000207_3):
    print(frame)

print(f'\nProtein Sequence: {proteins(frame)}')
