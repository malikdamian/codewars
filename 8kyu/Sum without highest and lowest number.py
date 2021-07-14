''' Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest element (the value, not the index!).
(The highest/lowest element is respectively only one element at each edge, even if there are more than one with the same value!)'''



def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr else 0