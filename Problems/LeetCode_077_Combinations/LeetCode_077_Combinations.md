# 【LeetCode】 077. Combinations

## Description
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

## Example:

```
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```

## Solution
* 與 LeetCode 077 相似, 用 DFS 方法。

### Code
```python
class Solution:
    def __init__(self):
        self.res = []

    def combine(self, n: "int", k: "int") -> "List[List[int]]":
        self.find(1, n, [], k)
        return self.res


    def find(self, start, n, tempAns, k):
        if len(tempAns) == k:
            self.res.append(tempAns)
        else:
            for i in range(start, n+1):
                self.find(i+1, n, tempAns+[i], k)
```

###### tags: `LeetCode` `python` `Combinations` 