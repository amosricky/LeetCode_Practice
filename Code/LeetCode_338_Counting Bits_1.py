class Solution:
    def countBits(self, num: 'int') -> 'List[int]':
        res = []
        for n in range(num+1):
            nStr = bin(n)
            res.append(nStr.count("1"))
        return res


myClass = Solution()
result = myClass.countBits(5)
print(result)
