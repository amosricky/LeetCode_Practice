# 【LeetCode】 491. Increasing Subsequences

## Description
Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.

Note:

+ The length of the given array will not exceed 15.
+ The range of integer in the given array is [-100,100].
+ The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

## Example:
```
Input: [4, 6, 7, 7]
Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
```

## Solution
* Brute Force 求解, 將符合條件的依序加入 res list 中。
* 最後在取出 len(2) >= 2 的 answer。

### Code
```python
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
```

###### tags: `LeetCode` `python` `Increasing Subsequences` 