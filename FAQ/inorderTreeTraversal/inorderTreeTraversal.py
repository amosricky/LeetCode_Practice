class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.recurRes = []

    def inorderRecur(self, root: "TreeNode"):
        if root.left is not None:
            self.inorderRecur(root.left)
        self.recurRes.append(root.val)
        if root.right is not None:
            self.inorderRecur(root.right)
        return self.recurRes

    def inorderNonRecur(self, root: "TreeNode"):
        nonRecurRes = []
        stack = []
        cur = root

        while True:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            elif not cur and len(stack) != 0:
                cur = stack.pop()
                nonRecurRes.append(cur.val)
                cur = cur.right
            else:
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
res = myClass.inorderRecur(root)
print(res)
res = myClass.inorderNonRecur(root)
print(res)
