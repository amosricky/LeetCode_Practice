# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: 'TreeNode') -> 'bool':
        res = True
        if not root:
            return res
        if not root.left and not root.right:
            return res

        nodes = [root.left, root.right]
        while nodes:
            temp = []
            for node in nodes:
                depLeft = self.maxDep(node.left)
                depRight = self.maxDep(node.right)
                if abs(depLeft - depRight) > 1:
                    res = False
                    return res
                elif node.left and node.right:
                    temp.append(node.left)
                    temp.append(node.right)
            nodes = temp
        return res

    def maxDep(self, node: 'TreeNode') -> 'int':
        if not node:
            return 0
        return 1 + max(self.maxDep(node.left), self.maxDep(node.right))


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(3)
root.right.left = TreeNode(3)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(4)
root.right.left.left = TreeNode(4)
root.right.left.right = TreeNode(4)
root.left.left.left.left = TreeNode(5)
root.left.left.left.right = TreeNode(5)

myClass = Solution()
result = myClass.isBalanced(root)
print(result)
