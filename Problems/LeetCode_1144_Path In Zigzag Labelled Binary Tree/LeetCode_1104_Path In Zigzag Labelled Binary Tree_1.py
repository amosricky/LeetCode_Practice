import math


class Solution:
    def __init__(self):
        self.result = [1]

    def pathInZigZagTree(self, label: "int") -> "List[int]":

        node = label
        while node != 1:
            self.result.append(node)
            parent = self.findParent(node)
            if parent == 1:
                break
            node = parent
        return sorted(self.result)

    def findParent(self, nodeNum: "int") -> "int":
        step = 1
        column = 1
        parentNum = 1
        while 2 ** step - 1 < nodeNum:
            step += 1
        if step % 2 == 0:
            column = 2 ** step - nodeNum
        else:
            column = nodeNum - (2 ** (step - 1) - 1)

        if step != 1 and (step - 1) % 2 == 0:
            parentNum = 2 ** (step - 1) - math.ceil(column / 2)

        elif step != 1 and (step - 1) % 2 == 1:
            parentNum = 2 ** (step - 2) + math.ceil(column / 2) - 1

        return parentNum


myClass = Solution()
res = myClass.pathInZigZagTree(26)
print(res)
