class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        sum = 0
        maxIncrease = float("-inf")

        for num in nums:
            if sum > 0:
                sum += num
            else:
                sum = num
            maxIncrease = max(maxIncrease, sum)
        return maxIncrease



myClass = Solution()
# result = myClass.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
result = myClass.maxSubArray([-2, 3, 2])
print(result)
