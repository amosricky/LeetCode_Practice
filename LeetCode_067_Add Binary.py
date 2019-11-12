class Solution:
    def addBinary(self, a: 'str', b: 'str') -> 'str':
        sum = bin(int(a, 2) + int(b, 2))
        return str(sum)[2:]


myClass = Solution()
result = myClass.addBinary("11", "1")
print(result)
