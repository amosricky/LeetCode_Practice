# 【LeetCode】 046. Permutations

## Description
Given a collection of distinct integers, return all possible permutations.

## Example:

```
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

## Solution1
![](https://img-blog.csdn.net/20180408111808715?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3lpcWlhb3hpaHVp/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)
* 類似上圖原理, 固定某數，將它放在start位置，再對 start 之後的數列遞迴。
* 在遞迴完成之後，要將原來調換位置的兩個數換回來。

### Code1
```python
class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums):
        self.find(nums, 0)
        return self.res

    def find(self, nums, start):
        if start == len(nums):
            self.res.append(nums.copy())
        else:
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                self.find(nums, start + 1)
                nums[start], nums[i] = nums[i], nums[start]
```

## Solution2
* 透過遞迴依序將數值加入 tempANS。
* 因多了一些 pop(), append(), 故速度上差 Solution 原地置換的速度一些。

### Code2
```python
class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: 'List[int]') -> 'List[List[int]]':
        if not nums:
            return self.res
        self.find(nums, [])
        return self.res

    def find(self, remainingNums: 'List[int]', tempANS: 'List[int]'):
        for index, value in enumerate(remainingNums):
            tempNums = remainingNums[:]
            tempNums.pop(index)
            if len(tempNums):
                self.find(tempNums, tempANS + [value])
            else:
                self.res.append(tempANS + [value])
        return
```


###### tags: `LeetCode` `python` `Permutations` 