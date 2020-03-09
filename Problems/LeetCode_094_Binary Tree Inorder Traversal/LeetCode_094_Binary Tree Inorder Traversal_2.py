# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = []

    def inorderTraversal(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return self.res

        nodes = []
        point = root

        while point or nodes:
            while point:
                nodes.append(point)
                point = point.left

            node = nodes.pop()
            self.res.append(node.val)
            point = node.right

        return self.res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
myClass = Solution()
result = myClass.inorderTraversal(root)
print(result)

