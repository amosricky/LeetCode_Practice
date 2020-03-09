# 【LeetCode】 078. Subsets

## Description
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note : The solution set must not contain duplicate subsets.
## Example:
```
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

## Solution
* 產生一個subset，用來存放走到當前的狀況。
* 一個確定可以放進結果 res 的 subset，必須是將整個nums走完 (i == len(nums))
* 故每一步訪查會有兩個叉路 1.將當前遇到的數字置之不理，直接朝向下一個index走   2.先將當前遇到的數字加進subset中，再朝下一個index走
### Code
```python
class Solution:
    def subsets(self, nums: "List[int]") -> "List[List[int]]":
        res, subset = [], []
        self.backtrack(res, subset, nums, 0)
        return res

    def backtrack(self, res: "List[List[int]]", subset: "List[int]", nums: "List[int]", i: "int") -> None:
        if i == len(nums):
            res.append(subset.copy())
        else:
            self.backtrack(res, subset, nums, i + 1)
            subset.append(nums[i])
            self.backtrack(res, subset, nums, i + 1)
            subset.pop()
```

###### tags: `LeetCode` `python` `Subsets` 