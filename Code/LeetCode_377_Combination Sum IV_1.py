class Solution:
    def __init__(self):
        self.res = 0

    def combinationSum4(self, nums: "List[int]", target: "int") -> "int":
        self.find(nums, target)
        return self.res

    def find(self, nums, target):
        if target == 0:
            self.res += 1
            return
        if target < 0:
            return

        for num in nums:
            self.find(nums, target - num)


myClass = Solution()
result = myClass.combinationSum4([4, 2, 1], 32)
print(result)
