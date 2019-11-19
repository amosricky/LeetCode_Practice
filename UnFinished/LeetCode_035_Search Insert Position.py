class Solution:
    def searchInsert(self, nums: 'List[int]', target: 'int') -> 'int':

        for idx, val in enumerate(nums):
            if (val == target) or (val > target):
                return idx
        return len(nums)

# 效能差很多
# class Solution:
#     def searchInsert(self, nums: 'List[int]', target: 'int') -> 'int':
#
#         for i in range(0, len(nums)):
#             if (nums[i] == target) or (nums[i] > target):
#                 return i
#         return len(nums)

myClass = Solution()
result = myClass.searchInsert([1, 3, 5, 6], 0)
print(result)
