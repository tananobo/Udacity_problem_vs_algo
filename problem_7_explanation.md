This code intiates RouterTrie by calling Router() and add handler by calling Router.add_handler(path_name, handler_name). And also it can look up handler from path_mane.  <br>

Algorithm methodology: One kind of search tree (Trie). the Trie will contain a part of the http path at each node, building from the root node /. <br>

<class RouteTrie>
Time complexity: O(n) / the worst case. (ex. Trie has only one path or Trie has a lot of only first path.)  <br>
Space complexity: O(1) / no auxiliary valuable that vary depends on inputs is used. <br>

<class RouteTrieNode>
Time complexity: O(1) / function insert() can access directory dictionaly value using key<br>
Space complexity: O(n) / self.children = {} size is decided depends on inputs <br>

<class Router>
Time complexity: O(1) /  all function in this class use simple if statement or assigning new value into valuable <br>
Space complexity: O(1) / no auxiliary valuable that vary depends on inputs is used. <br>
