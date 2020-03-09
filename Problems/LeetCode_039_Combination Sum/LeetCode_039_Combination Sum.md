# 【LeetCode】 039. Combination Sum

## Description
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

+ All numbers (including target) will be positive integers.
+ The solution set must not contain duplicate combinations.
## Example:

```
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```

## Solution
* 以 DFS 方式搜尋。

### Code
```python
class Solution:
    def __init__(self):
        self.res = []

    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        candidates.sort()
        self.find(candidates, 0, target, [])
        return self.res

    def find(self, candidates, start, target, tempAns):
        if target == 0:
            self.res.append(tempAns)
        elif target < candidates[0]:
            return
        else:
            for i in range(start, len(candidates)):
                self.find(candidates, i, target - candidates[i], tempAns + [candidates[i]])
```

###### tags: `LeetCode` `python` `Combination Sum` 