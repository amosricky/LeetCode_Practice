# 【LeetCode】 238. Product of Array Except Self

## Description
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

## Example:

```
Input:  [1,2,3,4]
Output: [24,12,8,6]
```

## Solution
![](https://leetcode.com/problems/product-of-array-except-self/Figures/238/products.png)
* 以 L List 存放左側累積乘積(不包含當前 index)。
* 以 R List 存放右側累積乘積(不包含當前 index)。
* 最後 L[i] * R[i] 即為 res[i] 之值。

### Code
```python
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
```

###### tags: `LeetCode` `python` `Product of Array Except Self` 