# In-order Tree Traversal

## Description
Tree Traversals (In-order)

## Example:
![](https://media.geeksforgeeks.org/wp-content/cdn-uploads/2009/06/tree12.gif)
```
Inorder (Left, Root, Right) : 4 2 5 1 3
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

    def inorderRecur(self, root: "TreeNode"):
        if root.left is not None:
            self.inorderRecur(root.left)
        self.recurRes.append(root.val)
        if root.right is not None:
            self.inorderRecur(root.right)
        return self.recurRes
```
## Solution2
* Non-Recursive using stack。
```
1) Create an empty stack S.
2) Initialize current node as root
3) Push the current node to S and set current = current->left until current is NULL
4) If current is NULL and stack is not empty then 
     a) Pop the top item from stack.
     b) Print the popped item, set current = popped_item->right 
     c) Go to step 3.
5) If current is NULL and stack is empty then we are done.
```
```
            1
          /   \
        2      3
      /  \
    4     5

Step 1 Creates an empty stack: S = NULL

Step 2 sets current as address of root: current -> 1

Step 3 Pushes the current node and set current = current->left until current is NULL
     current -> 1
     push 1: Stack S -> 1
     current -> 2
     push 2: Stack S -> 2, 1
     current -> 4
     push 4: Stack S -> 4, 2, 1
     current = NULL

Step 4 pops from S
     a) Pop 4: Stack S -> 2, 1
     b) print "4"
     c) current = NULL /*right of 4 */ and go to step 3
Since current is NULL step 3 doesn't do anything. 

Step 4 pops again.
     a) Pop 2: Stack S -> 1
     b) print "2"
     c) current -> 5/*right of 2 */ and go to step 3

Step 3 pushes 5 to stack and makes current NULL
     Stack S -> 5, 1
     current = NULL

Step 4 pops from S
     a) Pop 5: Stack S -> 1
     b) print "5"
     c) current = NULL /*right of 5 */ and go to step 3
Since current is NULL step 3 doesn't do anything

Step 4 pops again.
     a) Pop 1: Stack S -> NULL
     b) print "1"
     c) current -> 3 /*right of 5 */  

Step 3 pushes 3 to stack and makes current NULL
     Stack S -> 3
     current = NULL

Step 4 pops from S
     a) Pop 3: Stack S -> NULL
     b) print "3"
     c) current = NULL /*right of 3 */  

Traversal is done now as stack S is empty and current is NULL. 
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

    def inorderNonRecur(self, root: "TreeNode"):
        nonRecurRes = []
        stack = []
        cur = root

        while True:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            elif not cur and len(stack) != 0:
                cur = stack.pop()
                nonRecurRes.append(cur.val)
                cur = cur.right
            else:
                return nonRecurRes
```

## Solution3
* Non-Recursive without using stack。
* [Morris traversal for Inorder](https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/)

###### tags: `python` `In-order Tree Traversal` 