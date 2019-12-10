# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class FindElements:

    def __init__(self, root: 'TreeNode'):
        self.root = root
        self.root.val = 0
        self.recoveredTree(self.root)

    def recoveredTree(self, rootNode: 'TreeNode'):
        if rootNode and rootNode.left:
            rootNode.left.val = (rootNode.val * 2) + 1
            self.recoveredTree(rootNode.left)
        if rootNode and rootNode.right:
            rootNode.right.val = (rootNode.val * 2) + 2
            self.recoveredTree(rootNode.right)

    def find(self, target: 'int') -> 'bool':

        targetBin = bin(target + 1)
        node = self.root
        res = False

        for val in targetBin[3:]:
            if not node:
                break
            if val == "0":
                node = node.left
            elif val == "1":
                node = node.right

        if node and node.val == target:
            res = True

        return res



rootNode = TreeNode(-1)
rootNode.right = TreeNode(-1)
rootNode.right.left = TreeNode(-1)
rootNode.right.left.left = TreeNode(-1)

myClass = FindElements(rootNode)
print(myClass.root.val)
print(myClass.root.right.val)
print(myClass.root.right.left.val)
print(myClass.root.right.left.left.val)

print(myClass.find(2))
print(myClass.find(3))
print(myClass.find(4))
print(myClass.find(5))

