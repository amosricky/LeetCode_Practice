# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
        res = False
        if not root:
            return res
        nums = [root]
        values = [root.val]

        while nums:
            tempNums = []
            tempValues = []
            for index, node in enumerate(nums):
                if node.left:
                    tempNums.append(node.left)
                    tempValues.append(node.left.val + values[index])
                if node.right:
                    tempNums.append(node.right)
                    tempValues.append(node.right.val + values[index])
                if not node.left and not node.right:
                    if values[index] == sum:
                        res = True
                        return res
            nums = tempNums
            values = tempValues
        return res


