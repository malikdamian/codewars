'''Remove all exclamation marks from the end of sentence.'''


import re

def remove(s):
    return re.sub('!+$', '', s)