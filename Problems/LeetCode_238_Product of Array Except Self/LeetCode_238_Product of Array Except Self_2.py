class Solution:
    def productExceptSelf(self, nums):
        left = [1] * len(nums)
        res = [1] * len(nums)

        for left_idx in range(1, len(nums)):
            left[left_idx] = left[left_idx - 1] * nums[left_idx - 1]

        right = 1
        for res_idx in range(len(nums) - 1, -1, -1):
            res[res_idx] = left[res_idx] * right
            right *= nums[res_idx]

        return res


myClass = Solution()
print(myClass.productExceptSelf([1, 2, 3, 4]))
