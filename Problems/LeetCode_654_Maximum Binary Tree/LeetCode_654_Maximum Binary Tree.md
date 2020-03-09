# 【LeetCode】 654. Maximum Binary Tree

## Description
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

1. The root is the maximum number in the array.
2. The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
3. The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Note:

+ The size of the given array will be in the range [1,1000].

## Example 1:
```
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1
```

## Solution1
* Recursive

### Code1
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: "List[int]") -> "TreeNode":
        if len(nums) == 0:
            return

        maxValue = max(nums)
        # Get index of max value
        maxValueIndex = max(range(len(nums)), key=nums.__getitem__)

        left = nums[:maxValueIndex]
        right = nums[maxValueIndex + 1:]

        maxTree = TreeNode(maxValue)
        maxTree.left = self.constructMaximumBinaryTree(left)
        maxTree.right = self.constructMaximumBinaryTree(right)

        return maxTree
```

## Solution2
* non-recursive

### Code2
```python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: "List[int]") -> "TreeNode":

        if not nums:
            return None
        stk = []
        last = None
        for num in nums:
            while stk and stk[-1].val < num:
                last = stk.pop()
            node = TreeNode(num)
            if stk:
                stk[-1].right = node
            if last:
                node.left = last
            stk.append(node)
            last = None
        return stk[0]
```

###### tags: `LeetCode` `python` `Maximum Binary Tree` 