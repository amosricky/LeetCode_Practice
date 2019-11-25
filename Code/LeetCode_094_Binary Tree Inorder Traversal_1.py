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


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
myClass = Solution()
result = myClass.inorderTraversal(root)
print(result)
