def rotated_array_search(input_list, number, low, high):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if low > high:
        return -1
    mid = (high + low) // 2
    if input_list[mid] == number:
        return mid
    if input_list[mid+1] <= number <= input_list[high]:
        return binary_serch(input_list, number, mid+1, high)
    if input_list[0] <= number <= input_list[mid-1]:
        return binary_serch(input_list, number, low, mid-1)
    if input_list[mid+1] > input_list[high]:
        return rotated_array_search(input_list, number, mid+1, high)
    else:
        return rotated_array_search(input_list, number, low, mid-1)

def binary_serch(input_list, number, low, high):
    # print(input_list, number, low, high)
    if high <= low + 1:
        if input_list[high] == number:
            return high
        elif input_list[low] == number:
            return low
        else:
            return -1
    mid = (high + low) // 2
    if input_list[mid] == number:
        return mid
    elif input_list[mid] > number:
        return binary_serch(input_list, number, low, mid)
    else:
        return binary_serch(input_list, number, mid, high)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number, 0, len(input_list) - 1):
        print("Pass")
    else:
        print(linear_search(input_list, number))
        print(rotated_array_search(input_list, number, 0, len(input_list) - 1))
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])