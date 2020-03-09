# 【LeetCode】 979. Distribute Coins in Binary Tree

## Description
Given the root of a binary tree with N nodes, each node in the tree has node.val coins, and there are N coins total.

In one move, we may choose two adjacent nodes and move one coin from one node to another.  (The move may be from parent to child, or from child to parent.)

Return the number of moves required to make every node have exactly one coin.

Note:

+ 1<= N <= 100
+ 0 <= node.val <= N

## Example1:
![](https://assets.leetcode.com/uploads/2019/01/18/tree1.png)
```
Input: [3,0,0]
Output: 2
Explanation: From the root of the tree, we move one coin to its left child, and one coin to its right child.
```

## Example2:
![](https://assets.leetcode.com/uploads/2019/01/18/tree2.png)
```
Input: [0,3,0]
Output: 3
Explanation: From the left child of the root, we move two coins to the root [taking two moves].  Then, we move one coin from the root of the tree to the right child.
```

## Example3:
![](https://assets.leetcode.com/uploads/2019/01/18/tree3.png)
```
Input: [1,0,2]
Output: 2
```

## Example4:
![](https://assets.leetcode.com/uploads/2019/01/18/tree4.png)
```
Input: [1,0,0,null,3]
Output: 4
```

## Solution
![](https://imgur.com/m47oAx9.png)
* 方法參考上圖, 以 DFS 方式搜尋。
* 紀錄每節點間 path 所需 "傳遞的次數"。
* 左子 + 右子 + 自身硬幣數 - 1(自己使用)。

### Code
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.ans = 0

    def distributeCoins(self, root):
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node:
            return 0
        L, R = self.dfs(node.left), self.dfs(node.right)
        self.ans += abs(L)
        self.ans += abs(R)
        return L + R + node.val - 1
```

###### tags: `LeetCode` `python` `Distribute Coins in Binary Tree` 