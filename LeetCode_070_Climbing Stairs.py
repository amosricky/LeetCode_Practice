# class Solution:
#     def climbStairs(self, n: 'int') -> 'int':
#         if n <= 2:
#             return n
#         else:
#             return self.climbStairs(n - 1) + self.climbStairs(n - 2)

class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        if n <= 2:
            return n

        res = [1, 2]
        start = 2
        while start < n:
            res.append(res[start - 1] + res[start - 2])
            start += 1
        return res[n - 1]


myClass = Solution()
result = myClass.climbStairs(6)
print(result)
