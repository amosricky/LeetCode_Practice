class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.ans = 0

    def distributeCoins(self, root):
        self.dfs(root)
        return self.ans

    def dfs(self, node):
        if not node:
            return 0
        L, R = self.dfs(node.left), self.dfs(node.right)
        self.ans += abs(L)
        self.ans += abs(R)
        return L + R + node.val - 1




root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(0)
# root = TreeNode(0)
# root.left = TreeNode(7)
# root.right = TreeNode(2)
# root.left.left = TreeNode(0)
# root.left.right = TreeNode(0)
# root.right.left = TreeNode(0)
# root.right.right = TreeNode(0)
# root.left.left.left = TreeNode(0)
# root.left.left.right = TreeNode(0)
# root = TreeNode(1)
# root.left = TreeNode(0)
# root.right = TreeNode(0)
# root.left.right = TreeNode(3)
# root = TreeNode(4)
# root.left = TreeNode(0)
# root.left.right = TreeNode(0)
# root.left.right.right = TreeNode(0)

myClass = Solution()
result = myClass.distributeCoins(root)
print(result)
