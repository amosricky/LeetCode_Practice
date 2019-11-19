class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
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
                self.res.append(tempANS + [value])
        return


myClass = Solution()
result = myClass.permute([1, 2, 3])
print(result)
