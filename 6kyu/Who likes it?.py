"""Implement the function which takes an namesay containing the names of people that like an item.
It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases."""


def likes(names):

    if len(names) == 1:
        result = '{} likes this'.format(*names)
    elif len(names) == 2:
        result = '{} and {} like this'.format(*names)
    elif len(names) == 3:
        result = '{}, {} and {} like this'.format(*names)
    elif len(names) > 3:
        result = '{}, {} and {others} others like this'.format(*names, others=(len(names)-2))
    else:
        result = 'no one likes this'
    return result
