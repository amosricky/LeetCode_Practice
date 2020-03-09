# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = 0

    def rangeSumBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'int':
        if L <= root.val <= R:
            self.res += root.val
            if root.left:
                self.rangeSumBST(root.left, L, R)
            if root.right:
                self.rangeSumBST(root.right, L, R)
        elif root.val > R:
            if root.left:
                self.rangeSumBST(root.left, L, R)
        else:
            if root.right:
                self.rangeSumBST(root.right, L, R)
        return self.res


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(18)
myClass = Solution()
result = myClass.rangeSumBST(root, 7, 15)
print(result)
