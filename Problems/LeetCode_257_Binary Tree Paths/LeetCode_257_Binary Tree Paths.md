# 【LeetCode】 257. Binary Tree Paths

## Description
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

## Example:

```
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
```

## Solution
* 以 DFS 方式搜尋。

### Code
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def binaryTreePaths(self, root: "TreeNode") -> "List[str]":

        if not root:
            return []
        self.backTracking(root, [root.val])
        return self.res

    def backTracking(self, node: "TreeNode", tmp: "List"):

        if node.left:
            self.backTracking(node.left, tmp + [node.left.val])

        if node.right:
            self.backTracking(node.right, tmp + [node.right.val])

        if not node.left and not node.right:
            self.res.append(" -> ".join([str(c) for c in tmp]))
```

###### tags: `LeetCode` `python` `Binary Tree Paths` 