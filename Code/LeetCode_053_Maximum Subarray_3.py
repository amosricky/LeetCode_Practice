class Solution:
    def maxSubArray(self, nums):
        def divide_and_conquer(nums, start, end):
            if start == end - 1:
                return nums[start], nums[start], nums[start], nums[start]

            mid = (start + end) // 2
            subStart_l, mid_l, subEnd_l, subSum_l = divide_and_conquer(nums, start, mid)
            subStart_r, mid_r, subEnd_r, subSum_r = divide_and_conquer(nums, mid, end)

            subStart = max(subStart_l, subSum_l + subStart_r)
            mid = max(mid_l, mid_r, subEnd_l + subStart_r)
            subEnd = max(subEnd_r, subSum_r + subEnd_l)
            subSum = subSum_l + subSum_r

            return subStart, mid, subEnd, subSum
        _, res, _, _ = divide_and_conquer(nums, 0, len(nums))
        return res


myClass = Solution()
result = myClass.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
result = myClass.maxSubArray([-2, 3, 2])
print(result)
