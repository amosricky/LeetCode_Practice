class Solution:
    def countAndSay(self, n: 'int') -> 'str':
        dic = {1: "1", 2: "11"}
        startPoint = 3

        while startPoint <= 30:
            targetStr = dic[startPoint - 1]
            stackStr = []
            stackLength = []
            regenStr = ''

            for element in targetStr:
                if len(stackStr) == 0:
                    stackStr.append(element)
                    stackLength.append(1)
                elif element == stackStr[-1]:
                    stackLength[-1] += 1
                else:
                    stackStr.append(element)
                    stackLength.append(1)
            while len(stackStr) != 0:
                regenStr += str(stackLength.pop(0))
                regenStr += stackStr.pop(0)

            dic[startPoint] = regenStr
            startPoint += 1
        return dic[n]


myClass = Solution()
result = myClass.countAndSay(4)
print(result)
