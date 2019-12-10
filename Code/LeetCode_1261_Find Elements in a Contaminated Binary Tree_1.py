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
        res = False
        nodeList = [self.root]

        while nodeList:
            tempList = []
            for node in nodeList:
                if node.val == target:
                    res = True
                    return res
                if node.left:
                    tempList.append(node.left)
                if node.right:
                    tempList.append(node.right)
            nodeList = tempList
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


