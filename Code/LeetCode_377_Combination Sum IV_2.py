class Solution(object):
    def combinationSum4(self, nums, target):
        nums, combs = sorted(nums), [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    combs[i] += combs[i - num]
        return combs[target]


myClass = Solution()
result = myClass.combinationSum4([1, 2, 3], 4)
print(result)
