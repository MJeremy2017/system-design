# Trie

- A trie is a tree-like data structure. 
- The root represents an empty string. 
- Each node stores a character and has 26 children, one for each possible character. 
- Each tree node represents a single word or a prefix string.

Use case Search engine completion. A trie with word frequencies.

![img_1.png](freq.png)

Time complexity of finding the top `k` words given a prefix of length `p`.

- Find the prefix in the trie `O(p)`.
- Find all valid child that is a word `O(c)` where `c` is the number of children.
- Sort them by frequency `O(clogc)`.

To reduce time complexity, we can cache the top-searched queries at every node `O(1)`.

**Update Trie**

- Option 1: Update the trie weekly. Once a new trie is created, the new trie replaces the old one.
- Option 2: Update individual trie node directly. One a child node has updated its count, all its ancestors need to be updated as well.