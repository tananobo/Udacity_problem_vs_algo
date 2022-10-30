
def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if not isinstance(number, int):
        print("Input must be integer!")
        return

    if number < 0:
        print("Input must be positive!")
        return

    low = 0
    high = number
    while high > low + 1:
        mid = (high + low) // 2
        if mid ** 2 == number:
            return mid
        elif mid ** 2 > number:
            high = mid
        else:
            low = mid
    return high if high ** 2 <= number else low

# TEST case1: normal integer include edge case 0 and too big number / all should be "Pass"
print("===TEST case1===")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")

# TEST case2: input = 0 [edge case]
print("===TEST case2===")
print ("Pass" if  (0 == sqrt(0)) else "Fail") # Pass

# TEST case3: input = 10**17 [edge case/too big number] 
print("===TEST case3===")
import math
print ("Pass" if  (int(math.sqrt(10**17)) == sqrt(10**17)) else "Fail") # Pass

# TEST case4: float number and str
print("===TEST case4===")
sqrt(0.1) # Input must be integer!
sqrt("string") # Input must be integer!
sqrt(None)

# TEST case5: minus number
print("===TEST case5===")
sqrt(-1) # Input must be positive!
