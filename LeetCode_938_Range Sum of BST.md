# 【LeetCode】 938. Range Sum of BST

## Description
> Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
>
> The binary search tree is guaranteed to have unique values.

Note:

+ The number of nodes in the tree is at most 10000.
+ The final answer is guaranteed to be less than 2^31.
## Example:

```
Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32


Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23
```

## Solution1
#### non-recursive 解法
* 從 root 開始一層層尋找，利用 list 存放欲搜尋之節點。
* 若 node.val > R ， 向左子樹找。
* 若 node.val < L ， 向右子樹找。

### Code1
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'int':
        if not root:
            return 0
        self.res = 0

        nodes = [root]
        while nodes:
            temp = []
            for node in nodes:
                if L <= node.val <= R:
                    self.res += node.val
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
                elif node.val > R and node.left:
                    temp.append(node.left)
                elif node.val < L and node.right:
                    temp.append(node.right)

            nodes = temp
        return self.res
```
## Solution2
#### recursive 解法
* 從 root node 開始尋找，若 L <= node.val <= R ， 可往左右子樹遞迴尋找。
* 若 node.val > R ， 向左子樹找。
* 若 node.val < L ， 向右子樹找。

### Code2
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = 0

    def rangeSumBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'int':
        if L <= root.val <= R:
            self.res += root.val
            if root.left:
                self.rangeSumBST(root.left, L, R)
            if root.right:
                self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            if root.left:
                self.rangeSumBST(root.left, L, R)
        else:
            if root.right:
                self.rangeSumBST(root.right, L, R)
        return self.res
```

###### tags: `LeetCode` `python` `Range Sum of BST` 