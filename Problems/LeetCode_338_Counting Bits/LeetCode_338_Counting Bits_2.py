class Solution:
    def countBits(self, num: 'int') -> 'List[int]':
        res = [0] * (num + 1)
        for n in range(1, num + 1):
            if n % 2 == 0:
                res[n] = res[n//2]
            else:
                res[n] = int(res[(n-1)//2])+1
        return res


myClass = Solution()
result = myClass.countBits(5)
print(result)
