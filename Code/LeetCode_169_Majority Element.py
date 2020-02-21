import random

class Solution:
    # Dictionary
    def majorityElement1(self, nums: "List[int]") -> "int":
        target = len(nums) / 2
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
            if count[num] >= target:
                return num

    # Sorting
    def majorityElement2(self, nums: "List[int]") -> "int":
        nums.sort()
        return nums[len(nums) // 2]

    # Random
    def majorityElement3(self, nums: "List[int]") -> "int":

        while True:
            target = random.choice(nums)
            if nums.count(target) > len(nums)//2:
                return target

    # Boyer-Moore Voting Algorithm
    def majorityElement4(self, nums: "List[int]") -> "int":
        count = 1
        res = nums[0]

        for i in range(1, len(nums)):
            if res == nums[i]:
                count += 1
            elif count == 0:
                count = 1
                res = nums[i]
            else:
                count -= 1

        return res

    # Divide and Conquer
    def majorityElement5(self, nums: "List[int]") -> "int":
        def majority(start, end):
            if start == end:
                return nums[start]

            mid = (start + end)//2
            left = majority(start, mid)
            right = majority(mid+1, end)

            if left == right:
                return left

            leftCount = nums[start:end+1].count(left)
            rightCount = nums[start:end+1].count(right)

            return left if leftCount > rightCount else right

        return majority(0, len(nums)-1)

myClass = Solution()
result = myClass.majorityElement5([2,2,1,1,1,2,2])
print(result)
