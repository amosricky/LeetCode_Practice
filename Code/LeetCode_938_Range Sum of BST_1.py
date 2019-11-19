# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rangeSumBST(self, root: 'TreeNode', L: 'int', R: 'int') -> 'int':
        if not root:
            return 0
        self.res = 0

        nodes = [root]
        while nodes:
            temp = []
            for node in nodes:
                if L <= node.val <= R:
                    self.res += node.val
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
                elif node.val > R and node.left:
                    temp.append(node.left)
                elif node.val < L and node.right:
                    temp.append(node.right)

            nodes = temp
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
