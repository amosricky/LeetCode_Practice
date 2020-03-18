# 【LeetCode】 022. Generate Parentheses

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
* Recursive。

### Code1
```python
class Solution:
    def __init__(self):
        self.res = []

    def generateParenthesis(self, n: 'int') -> 'List[str]':
        self.add("", n)
        return self.res

    def add(self, tmp: 'str', n: 'int'):
        if len(tmp) == n*2 and tmp.count("(") == tmp.count(")") == n:
            self.res.append(tmp)
        else:
            L = tmp.count("(")
            R = tmp.count(")")

            if L >= R + 1 and R + 1 <= n:
                self.add(tmp + ")", n)
            if L + 1 >= R and L + 1 <= n:
                self.add(tmp + "(", n)
```
## Solution2
* Non-Recursive。

### Code2
```python
class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        if n == 0:
            return []
        parenthesisLists = ["("]
        start = 2
        while start <= 2 * n:
            tempParenthesisLists = []
            for parenthesisList in parenthesisLists:
                if parenthesisList.count("(") < n:
                    tempAppendLeft = parenthesisList + "("
                    if self.isLegal(tempAppendLeft):
                        tempParenthesisLists.append(tempAppendLeft)
                if parenthesisList.count(")") < n:
                    tempAppendRight = parenthesisList + ")"
                    if self.isLegal(tempAppendRight):
                        tempParenthesisLists.append(tempAppendRight)
            parenthesisLists = tempParenthesisLists
            start += 1
        return parenthesisLists

    def isLegal(self, target: 'List[str]') -> 'bool':
        countLeft = target.count("(")
        countRight = target.count(")")
        return countLeft >= countRight
```

###### tags: `LeetCode` `python` `Generate Parentheses` 