class Solution:
    def findSubsequences(self, nums: "List[int]") -> "List[List[int]]":
        res = []
        for _, num in enumerate(nums):
            for _, tmp in enumerate(res[:]):
                if num >= tmp[-1] and tmp + [num] not in res:
                    res.append(tmp + [num])

            if [num] not in res:
                res.append([num])

        return [i for i in res if len(i) > 1]


myClass = Solution()
result = myClass.findSubsequences([4, 6, 7, 7])
print(result)
