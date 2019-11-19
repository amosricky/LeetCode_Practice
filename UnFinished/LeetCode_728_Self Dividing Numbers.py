import math

class Solution:
    def selfDividingNumbers(self, left: 'int', right: 'int') -> 'List[int]':
        res = []
        for i in range(left, right + 1):
            if self.isDividingNumber(i):
                res.append(i)
        return res

    def isDividingNumber(self, num: 'int') -> 'bool':
        targets = list(str(num))
        res = True

        for target in targets:
            if int(target) == 0 or num % int(target) != 0:
                res = False
                return res
        return res


myClass = Solution()
result = myClass.selfDividingNumbers(1, 22)
print(result)
