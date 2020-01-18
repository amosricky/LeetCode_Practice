class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums):
        self.find(nums, 0)
        return self.res

    def find(self, nums, start):
        if start == len(nums):
            self.res.append(nums.copy())
        else:
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                self.find(nums, start + 1)
                nums[start], nums[i] = nums[i], nums[start]


myClass = Solution()
result = myClass.permute([1, 2, 3])
print(result)
