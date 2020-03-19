class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.recurRes = []

    def preorderRecur(self, root: "TreeNode"):
        self.recurRes.append(root.val)
        if root.left is not None:
            self.preorderRecur(root.left)
        if root.right is not None:
            self.preorderRecur(root.right)
        return self.recurRes

    def preorderNonRecur(self, root: "TreeNode"):
        nonRecurRes = []
        stack = [root]

        while len(stack) > 0:
            node = stack.pop(0)
            nonRecurRes.append(node.val)
            if node.right:
                stack.insert(0, node.right)
            if node.left:
                stack.insert(0, node.left)

        return nonRecurRes



root = TreeNode("x")
root.left = TreeNode("+")
root.left.left = TreeNode("-")
root.left.right = TreeNode("3")
root.left.left.left = TreeNode("1")
root.left.left.right = TreeNode("2")
root.right = TreeNode("+")
root.right.left = TreeNode("8")
root.right.right = TreeNode("/")
root.right.right.left = TreeNode("4")
root.right.right.right = TreeNode("2")

myClass = Solution()
res = myClass.preorderRecur(root)
print(res)
res = myClass.preorderNonRecur(root)
print(res)