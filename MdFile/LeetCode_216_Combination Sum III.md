# 【LeetCode】 216. Combination Sum III

## Description
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

+ All numbers (including target) will be positive integers.
+ The solution set must not contain duplicate combinations.
## Example:

```
Input: k = 3, n = 7
Output: [[1,2,4]]

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
```

## Solution
* 以 DFS 方式搜尋。

### Code
```python
class Solution:
    def __init__(self):
        self.res = []

    def combinationSum3(self, k: "int", n: "int") -> "List[List[int]]":
        self.find(1, k, n, [])
        return self.res

    def find(self, start, k, n, tempAns):
        if k == 0 and n == 0:
            self.res.append(tempAns)
            return
        elif n < 0 or k < 0:
            return

        for i in range(start, 10):
            self.find(i+1, k-1, n-i, tempAns+[i])
```

###### tags: `LeetCode` `python` `Combination Sum III` 