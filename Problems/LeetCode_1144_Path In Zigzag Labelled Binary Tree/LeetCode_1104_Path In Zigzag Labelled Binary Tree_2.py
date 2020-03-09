import math


class Solution:
    def pathInZigZagTree(self, label: "int") -> "List[int]":
        depth = int(math.log(label, 2)) + 1
        nodeIndex = 0
        nodeList = []

        if depth % 2 == 0:
            nodeIndex = (2 ** depth) - 1 - label
        else:
            nodeIndex = label - (2 ** (depth - 1))

        nodeList.insert(0, label)

        for step in range(depth - 1, 0, -1):
            nodeIndex = int(nodeIndex/2)
            if step % 2 == 0:
                nodeList.insert(0, 2 ** step - 1 - nodeIndex)
            else:
                nodeList.insert(0, 2 ** (step - 1) + nodeIndex)

        return nodeList


myClass = Solution()
res = myClass.pathInZigZagTree(13)
print(res)
