from itertools import groupby
import re

def encode(string):
    return ''.join(
        [''.join([str(len(list(group))), name]) for name, group in groupby(string)]
    )

def decode(compressed_string):
    match = re.compile('(\d+)([a-zA-Z])')
    return ''.join([int(x[0])*x[1] for x in match.findall(compressed_string)])
