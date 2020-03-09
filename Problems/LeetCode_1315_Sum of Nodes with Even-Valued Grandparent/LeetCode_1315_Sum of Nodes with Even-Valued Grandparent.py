class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumEvenGrandparent(self, root: "TreeNode") -> "int":
        result = 0
        nodes = [root]

        def check(checkNode):
            count = 0
            if checkNode.val % 2 != 0:
                return count
            if checkNode.left and checkNode.left.left:
                count += checkNode.left.left.val
            if checkNode.left and checkNode.left.right:
                count += checkNode.left.right.val
            if checkNode.right and checkNode.right.left:
                count += checkNode.right.left.val
            if checkNode.right and checkNode.right.right:
                count += checkNode.right.right.val
            return count

        while nodes:
            tempNodes = []
            for node in nodes:
                result += check(node)
                if node.left:
                    tempNodes.append(node.left)
                if node.right:
                    tempNodes.append(node.right)
            nodes = tempNodes

        return result


root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(9)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
myClass = Solution()
result = myClass.sumEvenGrandparent(root)
print(result)