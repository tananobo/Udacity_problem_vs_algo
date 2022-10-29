def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_list = mergesort(input_list)
    int1 = 0
    int2 = 0
    for i, num in enumerate(sorted_list):
        if i % 2 == 0:
            int1 += num * 10 ** (i // 2)
        else:
            int2 += num * 10 ** (i // 2)
    return int1, int2

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    print(f"output: {output}", f"solution:{solution}")
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
# test_case1: Udacity provided
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case) # True: sum should be 1816

# test_case2: min case
test_case = [[0, 0], [0, 0]]
test_function(test_case) # True: sum should be 0

# test_case3: long case
test_case = [[0,9,1,8,2,7,3,6,4,5],[97531,86420]]
test_function(test_case) # True: sum should be 183951
