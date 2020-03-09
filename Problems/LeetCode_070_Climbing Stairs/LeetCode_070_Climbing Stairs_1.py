class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        if n <= 2:
            return n
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


myClass = Solution()
result = myClass.climbStairs(6)
print(result)
