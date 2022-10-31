This code can find the index of serched number from roateted array. <br>

Algorithm methodology: Devide-and-Conquer and Binary search <br>
Time complexity: O(log(n)) / Because the code devide list into two half-length lists and abandon non-candidate one every time and recursion again until find the number. <br>
Space complexity: O(n) for storing input list (size = n) and O(1) for storing some auxiliary variables named high, low, mid (each size = 1). <br>
