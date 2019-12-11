# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST(self, root: 'TreeNode', val: 'int') -> 'TreeNode':

        if root.val and root.val < val:
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
        elif root.val and root.val > val:
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)

        return root


rootNode = TreeNode(4)
rootNode.left = TreeNode(2)
rootNode.right = TreeNode(7)
rootNode.left.left = TreeNode(1)
rootNode.left.right = TreeNode(3)
myClass = Solution()
result = myClass.insertIntoBST(rootNode, 5)
print(result)
