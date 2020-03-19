# Post-order Tree Traversal

## Description
Tree Traversals (Post-order)

## Example:
![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/2009/06/tree12.gif)
```
Preorder (Left, Root, Right) : 4 5 2 3 1
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

    def postorderRecur(self, root: "TreeNode"):
        if root.left is not None:
            self.postorderRecur(root.left)
        if root.right is not None:
            self.postorderRecur(root.right)
        self.recurRes.append(root.val)
        return self.recurRes
```
## Solution2
* Non-Recursive using stack。
```
Following is a simple stack based iterative process to print Postorder traversal.
1) Create an empty stack nodeStack and push root node to stack.
2) Do following while nodeStack is not empty.
….a) Pop an item from stack and print it.
….b) Push left child of popped item to stack
….c) Push right child of popped item to stack

Left child is pushed before right child to make sure that value in right subtree be pop and insert into the list first.
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

    def postorderNonRecur(self, root: "TreeNode"):
        nonRecurRes = []
        stack = [root]

        while len(stack) > 0:
            node = stack.pop(0)
            nonRecurRes.insert(0, node.val)
            if node.left:
                stack.insert(0, node.left)
            if node.right:
                stack.insert(0, node.right)

        return nonRecurRes
```

## Solution3
* Non-Recursive without using stack (DFS)。

### Code3
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.recurRes = []

    def postorderNonRecur2(self, root: "TreeNode"):
        nonRecurRes = []
        point = root
        visited = set()
        while (point and point not in visited):
            # Visited left subtree
            if (point.left and point.left not in visited):
                point = point.left

                # Visited right subtree
            elif (point.right and point.right not in visited):
                point = point.right

            else:
                nonRecurRes.append(point.val)
                visited.add(point)
                point = root

        return nonRecurRes
```

## Solution4
* Non-Recursive without using 2 stack。
```
1. Push root to first stack.
2. Loop while first stack is not empty
   2.1 Pop a node from first stack and push it to second stack
   2.2 Push left and right children of the popped node to first stack
3. Print contents of second stack
```

### Code4
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.recurRes = []

    def postorderNonRecur3(self, root: "TreeNode"):
        nonRecurRes = []
        if root is None:
            return

        # Create two stacks
        s1 = []
        s2 = []

        # Push root to first stack
        s1.append(root)

        # Run while first stack is not empty
        while s1:
            # Pop an item from s1 and
            # append it to s2
            node = s1.pop()
            s2.append(node)

            # Push left and right children of
            # removed item to s1
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)

                # Print all elements of second stack
        while s2:
            node = s2.pop()
            nonRecurRes.append(node.val)
        return nonRecurRes
```

###### tags: `python` `Post-order Tree Traversal` 