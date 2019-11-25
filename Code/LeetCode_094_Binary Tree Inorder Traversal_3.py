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
        if not root:
            return self.res

        cur = root
        while cur:
            if not cur.left:
                self.res.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right

                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                elif pre.right == cur:
                    self.res.append(cur.val)
                    cur = cur.right
        return self.res




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
myClass = Solution()
result = myClass.inorderTraversal(root)
print(result)

