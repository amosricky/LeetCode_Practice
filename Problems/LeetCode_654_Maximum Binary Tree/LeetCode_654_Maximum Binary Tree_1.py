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


myClass = Solution()
result = myClass.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
print(result)
