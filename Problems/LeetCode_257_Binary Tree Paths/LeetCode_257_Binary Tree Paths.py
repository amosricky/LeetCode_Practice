# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def binaryTreePaths(self, root: "TreeNode") -> "List[str]":

        if not root:
            return []
        self.backTracking(root, [root.val])
        return self.res

    def backTracking(self, node: "TreeNode", tmp: "List"):

        if node.left:
            self.backTracking(node.left, tmp + [node.left.val])

        if node.right:
            self.backTracking(node.right, tmp + [node.right.val])

        if not node.left and not node.right:
            self.res.append(" -> ".join([str(c) for c in tmp]))




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
myClass = Solution()
result = myClass.binaryTreePaths(root)
print(result)
