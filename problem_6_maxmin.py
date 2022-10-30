def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if not isinstance(ints, list) or len(ints) < 1:
        print("You must input correct list that length is at least 1!")
        return
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

# TEST case 1 : random order list elements are 0 to 9 (min, max) = (0, 9)
print("===TEST case1===")
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail") # Pass

# TEST case 2 : minimum input only [0] (min, max) = (0, 0)
print("===TEST case2===")
print ("Pass" if ((0, 0) == get_min_max([0])) else "Fail") # Pass

# TEST case 3 : empty list
print("===TEST case3===")
output = get_min_max([]) # You must input correct list that length is at least 1!
print(output) # None