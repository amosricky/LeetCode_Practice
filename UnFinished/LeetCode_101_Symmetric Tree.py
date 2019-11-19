# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: 'TreeNode') -> "bool":
        if not root:
            return True
        elif not root.left and not root.right:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left: 'TreeNode', right: 'TreeNode') -> 'bool':
        res = True
        if (left and not right) or (not left and right):
            res = False
            return res
        elif not left and not right:
            return res

        if left.val != right.val:
            res = False
            return res
        else:
            res = self.isMirror(left.left, right.right)
            if not res:
                return res
            res = self.isMirror(left.right, right.left)
            if not res:
                return res
        return res


root = TreeNode(1)
root.right = TreeNode(2)
myClass = Solution()
result = myClass.isSymmetric(root)
print(result)
