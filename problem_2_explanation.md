This code can find the index of serched number from roateted array. Time complexity is O(nlog(n)) because

Algorithm methodology: Devide-and-Conquer and Binary search
Time complexity: O(nlog(n)) / Because the code devide list into two half-length lists and abandon non-candidate one every time and recursion again until find the number. 
Space complexity: O(n) / The size of memory is keeped for input list (=n) and some fixed number of variables (high, low, mid).