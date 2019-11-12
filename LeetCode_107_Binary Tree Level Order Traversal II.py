# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []

        nodes = [root]
        value = [[root.val]]

        while nodes:
            temp = []
            tempVal = []
            for node in nodes:
                if node.left:
                    temp.append(node.left)
                    tempVal.append(node.left.val)
                if node.right:
                    temp.append(node.right)
                    tempVal.append(node.right.val)
            nodes = temp
            if tempVal:
                value.append(tempVal)
        return value[::-1]


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

myClass = Solution()
result = myClass.levelOrderBottom(root)
print(result)
