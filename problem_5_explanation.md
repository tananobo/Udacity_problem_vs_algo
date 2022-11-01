This code intiates Trie by calling Trie() and create word tier by calling trie.insert(word). And also it can look up prefix and return suffix candidate after prefix. <br>

Algorithm methodology: a tree-like data structure that stores a dynamic set of strings <br>

# class TrieNode
Time complexity: O(1) / function insert() can access directory dictionaly value using key.
Space complexity: O(n) / self.children = {} size is decided depends on inputs.
<br>

# class Trie
Time complexity: O(n) / function insert() and find() use for loop that iterate the input word (or prefix). So, time coplexity is decided input word length.
Space complexity: O(1) / no auxiliary valuable that vary depends on inputs is used.
