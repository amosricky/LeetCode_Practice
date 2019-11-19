# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        res = True
        if p and q:
            if p.val != q.val:
                res = False
                return res
            else:
                res = self.isSameTree(p.left, q.left)
                if not res:
                    return res
                res = self.isSameTree(p.right, q.right)
                if not res:
                    return res
        elif (p and not q) or (not p and q):
            res = False
            return res
        return res

