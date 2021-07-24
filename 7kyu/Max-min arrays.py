'''In this Kata, you will be given an array of unique elements, and your task is to rearrange the values so that the first max value is followed by the first minimum,
followed by second max value then second min value, etc.

For example:

solve([15,11,10,7,12]) = [15,7,12,10,11]
The first max is 15 and the first min is 7. The second max is 12 and the second min is 10 and so on.

More examples in the test cases.

Good luck!'''


def solve(arr):
    arr.sort()
    tmp = []
    for _ in range(len(arr)//2):
        tmp.append(max(arr))
        arr.pop(-1)
        tmp.append(min(arr))
        arr.pop(0)
    return tmp + arr