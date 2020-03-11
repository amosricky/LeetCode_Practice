class Solution:
    def productExceptSelf(self, nums: "List[int]") -> "List[int]":
        L = [0] * len(nums)
        L[0] = 1
        for i in range(1, len(nums)):
            L[i] = L[i-1] * nums[i-1]

        R = [0] * len(nums)
        R[-1] = 1
        for j in range(len(nums) - 2, -1, -1):
            R[j] = R[j + 1] * nums[j+1]

        res = [0] * len(nums)
        for k in range(0, len(res)):
            res[k] = L[k] * R[k]

        return res





myClass = Solution()
res = myClass.productExceptSelf([1,2,3,4])
print(res)