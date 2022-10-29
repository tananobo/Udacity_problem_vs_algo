def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    loc0 = 0
    loc2 = len(input_list) - 1
    current = 0
    while current <= loc2:
        if input_list[current] == 0:
            input_list[loc0], input_list[current] = input_list[current], input_list[loc0]
            loc0 += 1
            current += 1
        elif input_list[current] == 2:
            input_list[loc2], input_list[current] = input_list[current], input_list[loc2]
            loc2 -= 1
        else:
            current += 1
    return input_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# TEST1: Udacity provided Ahem. all should be passed.
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])

# TEST2: empty -> output [] and Pass
test_function([])

# TEST3: single number -> output [same num] and Pass 
test_function([0])
test_function([1])
test_function([2])