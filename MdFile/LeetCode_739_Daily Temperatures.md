# 【LeetCode】 739. Daily Temperatures

## Description
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note:
+ The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].

## Solution1
* Use stack

### Code1
```python
class Solution:
    def dailyTemperatures(self, T: "List[int]") -> "List[int]":
        result = [0] * len(T)
        stack = []

        for i in range(len(T)-1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack and T[i] < T[stack[-1]]:
                result[i] = stack[-1] - i
            stack.append(i)

        return result
```

###### tags: `LeetCode` `python` `Daily Temperatures` 