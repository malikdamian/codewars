'''Given an array of numbers (in string format), you must return a string. The numbers correspond to the letters of the alphabet in reverse order: a=26, z=1 etc. You should also account for '!', '?' and ' ' that are represented by '27', '28' and '29' respectively.

All inputs will be valid.'''


import string


def switcher(arr):
    return ''.join(list(reversed(f'{" "}{"?"}{"!"}{string.ascii_lowercase}'))[int(n) - 1] for n in arr)