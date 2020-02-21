# 【LeetCode】 169. Majority Element

## Description
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

## Example 1:
```
Input: [3,2,3]
Output: 3
```

## Example 2:
```
Input: [2,2,1,1,1,2,2]
Output: 2
```

## Solution1
* Dictionary
* 循環一次, 以 dictionary 紀錄每個值出現次數

### Code1
```python
class Solution:
    def majorityElement1(self, nums: "List[int]") -> "int":
        target = len(nums) / 2
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
            if count[num] >= target:
                return num
```

## Solution2
* Sorting
* 排序, 因題意說明 majority > n/2, 故排序後中位數一定為解

### Code2
```python
class Solution:
    def majorityElement2(self, nums: "List[int]") -> "int":
        nums.sort()
        return nums[len(nums) // 2]
```

## Solution3
* Random
* 亂數取值後 count 其個數

### Code3
```python
import random
class Solution:
    def majorityElement3(self, nums: "List[int]") -> "int":
        while True:
            target = random.choice(nums)
            if nums.count(target) > len(nums)//2:
                return target
```

## Solution4
* Boyer-Moore Voting Algorithm
* 投票演算法

### Code4
```python
class Solution:
    def majorityElement4(self, nums: "List[int]") -> "int":
        count = 1
        res = nums[0]

        for i in range(1, len(nums)):
            if res == nums[i]:
                count += 1
            elif count == 0:
                count = 1
                res = nums[i]
            else:
                count -= 1

        return res
```

## Solution5
* Divide and Conquer

### Code5
```python
class Solution:
    def majorityElement5(self, nums: "List[int]") -> "int":
        def majority(start, end):
            if start == end:
                return nums[start]

            mid = (start + end)//2
            left = majority(start, mid)
            right = majority(mid+1, end)

            if left == right:
                return left

            leftCount = nums[start:end+1].count(left)
            rightCount = nums[start:end+1].count(right)

            return left if leftCount > rightCount else right

        return majority(0, len(nums)-1)
```

###### tags: `LeetCode` `python` `Majority Element` 