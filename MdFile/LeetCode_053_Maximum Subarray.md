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

###### tags: `LeetCode` `python` `Maximum Subarray` 