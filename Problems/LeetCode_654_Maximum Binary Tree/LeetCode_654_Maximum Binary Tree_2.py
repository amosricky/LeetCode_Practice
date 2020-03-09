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


myClass = Solution()
result = myClass.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
print(result)
