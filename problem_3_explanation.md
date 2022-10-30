This code will firstly sort number in order in the list by the merged sort way that I learned in Udacity course. After that, it will pick number one by one into two integer on each digit. It mean every time it pick numbers, 1 digit up (10 times larger than previous). The output should be two integer that sum must be maximum.

Algorithm methodology: Merge Sort
Time complexity: O(nlog(n)) / Because merge sort takes O(nlogn) and postprocess (picking number for every digit) takes O(n) so O(nlogn + n) = O(nlogn). 
Space complexity: O(n) / it need soreted result stored area.