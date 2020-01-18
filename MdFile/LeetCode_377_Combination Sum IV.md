# 【LeetCode】 377. Combination Sum IV

## Description
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Note:

+ All numbers (including target) will be positive integers.
+ The solution set must not contain duplicate combinations.
## Example:

```
nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.
```

## Solution1
* 以 DFS 方式搜尋。
* 但因為不斷遍歷所有數值, 容易 timeout.

### Code1
```python
class Solution:
    def __init__(self):
        self.res = 0

    def combinationSum4(self, nums: "List[int]", target: "int") -> "int":
        self.find(nums, target)
        return self.res

    def find(self, nums, target):
        if target == 0:
            self.res += 1
            return
        if target < 0:
            return

        for num in nums:
            self.find(nums, target - num)
```

## Solution2
![](https://imgur.com/euysrmc.png)
* 方法參考上圖, 以 Dynamic Programming 方式搜尋。

### Code2
```python
class Solution(object):
    def combinationSum4(self, nums, target):
        nums, combs = sorted(nums), [1] + [0] * target
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    combs[i] += combs[i - num]
        return combs[target]
```

###### tags: `LeetCode` `python` `Combination Sum IV` 