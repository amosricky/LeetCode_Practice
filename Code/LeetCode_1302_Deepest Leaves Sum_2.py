class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.stepSum = {}

    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.check(1, root)
        print(self.stepSum)
        return self.stepSum[max(self.stepSum.keys())]

    def check(self, step: "int", node: TreeNode):
        if not node:
            return
        if step not in self.stepSum.keys():
            self.stepSum[step] = node.val
        else:
            self.stepSum[step] += node.val
        self.check(step+1, node.left)
        self.check(step+1, node.right)



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