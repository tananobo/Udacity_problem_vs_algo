This code intiates RouterTrie by calling Router() and add handler by calling Router.add_handler(path_name, handler_name). And also it can look up handler from path_mane.  <br>

Algorithm methodology: One kind of search tree (Trie). the Trie will contain a part of the http path at each node, building from the root node /. not same as problem 5, there is a rapper class called "Routar" has two modular trie and node.<br>
Time complexity: O(n) / the worst case. (ex. Trie has only one path or Trie has a lot of only first path.)  <br>
Space complexity: O(1) / Because only one strings (path) is stored into memory for searching. <br>
