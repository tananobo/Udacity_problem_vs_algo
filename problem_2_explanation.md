This code can find the index of serched number from roateted array. <br>

Algorithm methodology: Devide-and-Conquer and Binary search <br>
Time complexity: O(log(n)) / Because the code devide list into two half-length lists and abandon non-candidate one every time and recursion again until find the number. <br>
Space complexity:  O(log(n)) / in each function, auxiliary variables named high, low, mid (each size = 1) are stored. And because of using recursive binary search function could be called potentially log(n) times <br>
