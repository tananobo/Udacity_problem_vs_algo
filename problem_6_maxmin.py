def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    maxnum = - 10 ** 9
    minnum = 10 ** 9
    for num in ints:
        if num > maxnum:
            maxnum = num
        if num < minnum:
            minnum = num
    return minnum, maxnum

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

print ("Pass" if ((0, 0) == get_min_max([0])) else "Fail")