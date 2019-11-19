class Solution:
    def __init__(self):
        self.res = []

    def permuteUnique(self, nums: 'List[int]') -> 'List[List[int]]':
        if not nums:
            return self.res
        self.find(nums, [])
        return self.res

    def find(self, remainingNums: 'List[int]', tempANS: 'List[int]'):
        for index, value in enumerate(remainingNums):
            tempNums = remainingNums[:]
            tempNums.pop(index)
            if len(tempNums):
                self.find(tempNums, tempANS + [value])
                continue
            else:
                if not tempANS + [value] in self.res:
                    self.res.append(tempANS + [value])
        return

# class Solution(object):
#     def permuteUnique(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         self.res = []
#         sub = []
#         nums = sorted(nums)
#         fl = [0] * len(nums)
#         self.dfs(nums, [], fl)
#         return self.res
#
#     def dfs(self, Nums, subList, flagList):
#         if len(subList) == len(Nums):
#             self.res.append(subList[:])
#         last = None
#         for idx in range(len(Nums)):
#             m = Nums[idx]
#             if flagList[idx] == 1:
#                 continue
#             if last == m:
#                 continue
#             flagList[idx] = 1
#             subList.append(m)
#             self.dfs(Nums, subList, flagList)
#             last = subList.pop()
#             flagList[idx] = 0

myClass = Solution()
result = myClass.permuteUnique([1, 1, 3])
print(result)
