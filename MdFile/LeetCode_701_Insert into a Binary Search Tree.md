# 【LeetCode】 701. Insert into a Binary Search Tree

## Description
Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

## Example:
```
Given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
```
You can return this binary search tree:
```
         4
       /   \
      2     7
     / \   /
    1   3 5
```
This tree is also valid:
```
         5
       /   \
      2     7
     / \   
    1   3
         \
          4
```

## Solution1
* non-recursive。

### Code1
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST(self, root: 'TreeNode', val: 'int') -> 'TreeNode':

        res = root
        point = res
        newNode = TreeNode(val)

        while point:
            if point.val and point.val < val:
                if point.right:
                    point = point.right
                else:
                    point.right = newNode
                    break
            elif point.val and point.val > val:
                if point.left:
                    point = point.left
                else:
                    point.left = newNode
                    break

        return res
```
## Solution2
* recursive。

### Code2
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST(self, root: 'TreeNode', val: 'int') -> 'TreeNode':

        if root.val and root.val < val:
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
        elif root.val and root.val > val:
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)

        return root
```

###### tags: `LeetCode` `python` `Insert into a Binary Search Tree` 