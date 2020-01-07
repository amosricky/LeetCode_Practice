# 【LeetCode】 560. Subarray Sum Equals K

## Description
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Note:

+ The length of the array is in range [1, 20,000].
+ The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

## Example 1:
```
Input:nums = [1,1,1], k = 2
Output: 2
```

## Solution1
* 以 List 儲存累加上去的 Sum。
* 每次判斷當前的 Sum 是否等於 K 。
* 若不為 K 則向前找有沒有 Sum - K。
* 只須 O(n) 但效能還不夠好 可再精進。

### Code1
```python
class Solution(object):
    def subarraySum(self, nums, k):
        sumList = []
        total = 0
        count = 0

        for index, num in enumerate(nums):
            total += num
            want = total - k
            if want == 0:
                count += 1
                count += sumList.count(0)
            elif want != 0 and want in sumList:
                count += sumList.count(want)
            sumList.append(total)
        return count
```

###### tags: `LeetCode` `python` `Subarray Sum Equals K` 