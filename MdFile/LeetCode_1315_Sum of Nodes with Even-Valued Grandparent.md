# 【LeetCode】 1315. Sum of Nodes with Even-Valued Grandparent

## Description
Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

Constraints:

+ The number of nodes in the tree is between 1 and 10^4.
+ The value of nodes is between 1 and 100.

## Example 1:
![](https://assets.leetcode.com/uploads/2019/07/24/1473_ex1.png)
```
Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
```

## Solution1
* 利用 stack 遍歷每一階層之節點進行搜尋。

### Code1
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumEvenGrandparent(self, root: "TreeNode") -> "int":
        result = 0
        nodes = [root]

        def check(checkNode):
            count = 0
            if checkNode.val % 2 != 0:
                return count
            if checkNode.left and checkNode.left.left:
                count += checkNode.left.left.val
            if checkNode.left and checkNode.left.right:
                count += checkNode.left.right.val
            if checkNode.right and checkNode.right.left:
                count += checkNode.right.left.val
            if checkNode.right and checkNode.right.right:
                count += checkNode.right.right.val
            return count

        while nodes:
            tempNodes = []
            for node in nodes:
                result += check(node)
                if node.left:
                    tempNodes.append(node.left)
                if node.right:
                    tempNodes.append(node.right)
            nodes = tempNodes

        return result
```

###### tags: `LeetCode` `python` `Sum of Nodes with Even-Valued Grandparent` 