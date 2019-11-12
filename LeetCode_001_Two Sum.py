class Solution:
    def twoSum(self, nums: 'List[int]', target: 'int') -> 'List[int]':
        numMap = {}
        for i in range(len(nums)):
            if (target-nums[i] in numMap):
                return [numMap[target-nums[i]],i]
            else:
                numMap[nums[i]] = i
        return "No Answer!"

testProblem = Solution()
testAnswer = testProblem.twoSum([2, 7, 11, 15],27)
print(testAnswer)

