# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        res = 1
        nodes = [root]

        while nodes:
            temp = []
            for node in nodes:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                if not node.left and not node.right:
                    return res

            res += 1
            nodes = temp


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

myClass = Solution()
result = myClass.minDepth(root)
print(result)
