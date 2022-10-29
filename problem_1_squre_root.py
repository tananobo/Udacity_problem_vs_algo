def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
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

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")