# 【LeetCode】 053. Maximum Subarray

## Description
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up:

+ If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
## Example:

```
Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

## Solution1
* 第一次 O(n) 寫法

### Code1
```python
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        sum = 0
        maxIncrease = float("-inf")

        for num in nums:
            if sum > 0:
                sum += num
            else:
                sum = num
            maxIncrease = max(maxIncrease, sum)
        return maxIncrease
```
## Solution2
* Dynamic Programming
* 累加當前的 max sum, 以 res 傳回

### Code2
```python
class Solution:
    def maxSubArray(self, nums: 'List[int]') -> 'int':
        current, pre = 0, 0
        res = float("-inf")

        for num in nums:
            current = num + (pre if pre > 0 else 0)
            pre = current
            res = max(res, current)

        return res
```

## Solution3
* Divide and Conquer
* subStart : max contiguous sum in nums[start:end] including the first value
* mid : max contiguous sum in nums[start:end] anywhere 
* subEnd : max contiguous sum in nums[start:end] including the last value
* subSum : the sum of all values in nums[start:end]

### Code1
```python
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
```

###### tags: `LeetCode` `python` `Maximum Subarray` 