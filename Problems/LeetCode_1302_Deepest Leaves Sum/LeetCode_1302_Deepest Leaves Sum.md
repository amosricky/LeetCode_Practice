# 【LeetCode】 1302. Deepest Leaves Sum

## Description
Given a binary tree, return the sum of values of its deepest leaves.

Constraints:

+ The number of nodes in the tree is between 1 and 10^4.
+ The value of nodes is between 1 and 100.

## Example 1:
![](https://assets.leetcode.com/uploads/2019/07/31/1483_ex1.png)
```
Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
```

## Solution1
* 利用兩個 stack 分別儲存該階層的 node 與 node.val。
* 若該階層存在子節點, 則 stack 重新紀錄。
* 確認該階層都沒子節點回傳儲存 node.val 之 stack sum。

### Code1
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return None

        node = [root]
        nodeVal = [root.val]

        while len(node) > 0:
            tempNode = []
            tempVal = []

            for _, value in enumerate(node):

                if value.left:
                    tempNode.append(value.left)
                    tempVal.append(value.left.val)
                if value.right:
                    tempNode.append(value.right)
                    tempVal.append(value.right.val)

            if len(tempNode) > 0:
                node = tempNode
                nodeVal = tempVal
            else:
                break
        return sum(nodeVal)
```
## Solution2
* 利用 python dictionary, 以 recursive 方式將各階層的 node.val 儲存於 dictionary 中。
* 以 example 為例會建出 {1: 1, 2: 5, 3: 15, 4: 15}, 最後回傳最後一階層 value。

### Code2
```python
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.stepSum = {}

    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.check(1, root)
        return self.stepSum[max(self.stepSum.keys())]

    def check(self, step: "int", node: TreeNode):
        if not node:
            return
        if step not in self.stepSum.keys():
            self.stepSum[step] = node.val
        else:
            self.stepSum[step] += node.val
        self.check(step+1, node.left)
        self.check(step+1, node.right)
```

###### tags: `LeetCode` `python` `Deepest Leaves Sum` 