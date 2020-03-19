# Pre-order Tree Traversal

## Description
Tree Traversals (In-order)

## Example:
![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/2009/06/tree12.gif)
```
Preorder (Left, Root, Right) : 1 2 4 5 3
```

## Solution1
* Recursive。

### Code1
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.recurRes = []

    def preorderRecur(self, root: "TreeNode"):
        self.recurRes.append(root.val)
        if root.left is not None:
            self.preorderRecur(root.left)
        if root.right is not None:
            self.preorderRecur(root.right)
        return self.recurRes
```
## Solution2
* Non-Recursive using stack。
```
Following is a simple stack based iterative process to print Preorder traversal.
1) Create an empty stack nodeStack and push root node to stack.
2) Do following while nodeStack is not empty.
….a) Pop an item from stack and print it.
….b) Push right child of popped item to stack
….c) Push left child of popped item to stack

Right child is pushed before left child to make sure that left subtree is processed first.
```

### Code2
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.recurRes = []

    def preorderNonRecur(self, root: "TreeNode"):
        nonRecurRes = []
        stack = [root]

        while len(stack) > 0:
            node = stack.pop(0)
            nonRecurRes.append(node.val)
            if node.right:
                stack.insert(0, node.right)
            if node.left:
                stack.insert(0, node.left)

        return nonRecurRes
```

## Solution3
* Non-Recursive without using stack。
* [Morris traversal for Preorder](https://www.geeksforgeeks.org/morris-traversal-for-preorder/)

###### tags: `python` `Pre-order Tree Traversal` 