class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        res = [1, 2]
        if n <= 2:
            return res[n-1]

        for i in range(3, n+1):
            val = res[i-3] + res[i-2]
            res.append(val)

        return res[n-1]


myClass = Solution()
result = myClass.climbStairs(6)
print(result)
