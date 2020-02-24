class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        current, pre = 0, 0
        res = float("-inf")

        for num in nums:
            current = num + (pre if pre > 0 else 0)
            pre = current
            res = max(res, current)

        return res


myClass = Solution()
result = myClass.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
print(result)
