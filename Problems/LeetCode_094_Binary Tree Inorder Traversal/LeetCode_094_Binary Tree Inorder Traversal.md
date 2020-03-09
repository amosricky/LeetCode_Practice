# 【LeetCode】 094. Binary Tree Inorder Traversal

## Description
Given a binary tree, return the inorder traversal of its nodes' values.

Follow up:

+ Recursive solution is trivial, could you do it iteratively?
## Example:

```
Example :

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
```

## Solution1
#### recursive 解法
* 遞迴求中序排序。

### Code1
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

    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if root.left:
            self.inorderTraversal(root.left)
        self.res.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)
        return self.res
```
## Solution2
#### non-recursive : 一般解法
* point 指向 root ，先将所指向的 node 加入 nodes，然后再将 point 指向 point.left ， 依序將所有左節點加入 nodes。
* 然後 pop 出 nodes 之 node，保存其值，再將 point 指向 node.right，若 point 存在 ，則在下次循環時又可将其所有左節點加入 nodes 中。

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
        self.res = []

    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return self.res

        nodes = []
        point = root

        while point or nodes:
            while point:
                nodes.append(point)
                point = point.left

            node = nodes.pop()
            self.res.append(node.val)
            point = node.right

        return self.res
```
## Solution3
#### non-recursive : Threaded Binary Tree (引線二元樹)解法

![](https://github.com/shenyun2304/swift-algorithm-club-zhTW/raw/master/Threaded%20Binary%20Tree/Images/Partial.png)
* 在一般二元樹中，每個 leaf node 的 左/右 子節點正常來說都是 nil 
* 而在引線二元樹中，每個 leaf node 的「左/右」子節點指向其中序排序的「前驅/後繼」節點。
* 而在此例中，主要將 leaf node 之 right 指向其中序排序的「後繼」節點來做中序排序。

### Code3
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

    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return self.res

        cur = root
        while cur:
            if not cur.left:
                self.res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right

                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                elif pre.right == cur:
                    self.res.append(cur.val)
                    cur = cur.right
        return self.res
```

###### tags: `LeetCode` `python` `Binary Tree Inorder Traversal` 