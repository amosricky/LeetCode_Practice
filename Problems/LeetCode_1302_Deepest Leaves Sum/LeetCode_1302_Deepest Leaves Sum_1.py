class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return None

        node = [root]
        nodeVal = [root.val]

        while len(node) > 0:
            tempNode = []
            tempVal = []

            for _, value in enumerate(node):

                if value.left:
                    tempNode.append(value.left)
                    tempVal.append(value.left.val)
                if value.right:
                    tempNode.append(value.right)
                    tempVal.append(value.right.val)

            if len(tempNode) > 0:
                node = tempNode
                nodeVal = tempVal
            else:
                break
        return sum(nodeVal)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.left = TreeNode(7)
root.right.right.right = TreeNode(8)
myClass = Solution()
result = myClass.deepestLeavesSum(root)
print(result)