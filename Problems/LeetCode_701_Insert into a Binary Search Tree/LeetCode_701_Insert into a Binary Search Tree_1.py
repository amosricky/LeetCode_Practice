# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST(self, root: 'TreeNode', val: 'int') -> 'TreeNode':

        res = root
        point = res
        newNode = TreeNode(val)

        while point:
            if point.val and point.val < val:
                if point.right:
                    point = point.right
                else:
                    point.right = newNode
                    break
            elif point.val and point.val > val:
                if point.left:
                    point = point.left
                else:
                    point.left = newNode
                    break

        return res


rootNode = TreeNode(4)
rootNode.left = TreeNode(2)
rootNode.right = TreeNode(7)
rootNode.left.left = TreeNode(1)
rootNode.left.right = TreeNode(3)
myClass = Solution()
result = myClass.insertIntoBST(rootNode, 5)
print(result)