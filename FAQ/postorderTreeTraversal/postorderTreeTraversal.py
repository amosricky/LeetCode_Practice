class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.recurRes = []

    def postorderRecur(self, root: "TreeNode"):
        if root.left is not None:
            self.postorderRecur(root.left)
        if root.right is not None:
            self.postorderRecur(root.right)
        self.recurRes.append(root.val)
        return self.recurRes

    def postorderNonRecur(self, root: "TreeNode"):
        nonRecurRes = []
        stack = [root]

        while len(stack) > 0:
            node = stack.pop(0)
            nonRecurRes.insert(0, node.val)
            if node.left:
                stack.insert(0, node.left)
            if node.right:
                stack.insert(0, node.right)

        return nonRecurRes

    def postorderNonRecur2(self, root: "TreeNode"):
        nonRecurRes = []
        point = root
        visited = set()
        while (point and point not in visited):
            # Visited left subtree
            if (point.left and point.left not in visited):
                point = point.left

                # Visited right subtree
            elif (point.right and point.right not in visited):
                point = point.right

            else:
                nonRecurRes.append(point.val)
                visited.add(point)
                point = root

        return nonRecurRes

    def postorderNonRecur3(self, root: "TreeNode"):
        nonRecurRes = []
        if root is None:
            return

        # Create two stacks
        s1 = []
        s2 = []

        # Push root to first stack
        s1.append(root)

        # Run while first stack is not empty
        while s1:
            # Pop an item from s1 and
            # append it to s2
            node = s1.pop()
            s2.append(node)

            # Push left and right children of
            # removed item to s1
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)

                # Print all elements of second stack
        while s2:
            node = s2.pop()
            nonRecurRes.append(node.val)
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
res = myClass.postorderRecur(root)
print(res)
res = myClass.postorderNonRecur(root)
print(res)
res = myClass.postorderNonRecur2(root)
print(res)
res = myClass.postorderNonRecur3(root)
print(res)