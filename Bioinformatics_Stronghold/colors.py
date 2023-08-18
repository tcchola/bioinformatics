def colored(sequence):
    """Will color each numcleotide"""
    colors = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[91m',
        'reset': '\033[0;0m',
    }

    string = ""

    for nucleotide in sequence:
        if nucleotide in colors:
            string += colors[nucleotide] + nucleotide
        else:
            string += colors['reset'] + nucleotide
    return string + '\033[0;0m'
