# 【LeetCode】 040. Combination Sum II

## Description
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

+ All numbers (including target) will be positive integers.
+ The solution set must not contain duplicate combinations.
## Example:

```
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
```

## Solution
* 以 DFS 方式搜尋。

### Code
```python
class Solution:
    def __init__(self):
        self.res = []

    def combinationSum2(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        if not target:
            return []
        candidates.sort()
        self.find(candidates, target, [])
        return self.res

    def find(self, remaining: 'List[int]', target: 'int', tempANS: 'List[int]'):

        for index, value in enumerate(remaining):
            if value < target and index < len(remaining) - 1:
                self.find(remaining[index + 1:], target - value, tempANS + [value])
                continue
            elif value == target:
                if not (tempANS + [value]) in self.res:
                    self.res.append(tempANS + [value])
                return
            return
```

###### tags: `LeetCode` `python` `Combination Sum II` 