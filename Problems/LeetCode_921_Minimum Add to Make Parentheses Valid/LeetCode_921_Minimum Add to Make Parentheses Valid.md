# 【LeetCode】 921. Minimum Add to Make Parentheses Valid

## Description
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.

Formally, a parentheses string is valid if and only if:

* It is the empty string, or
* It can be written as AB (A concatenated with B), where A and B are valid strings, or
* It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

Note:

+ S.length <= 1000
+ S only consists of '(' and ')' characters.

## Example1:
```
Input: "())"
Output: 1
```
## Example2:
```
Input: "((("
Output: 3
```
## Example3:
```
Input: "()"
Output: 0
```
## Example4:
```
Input: "()))(("
Output: 4
```

## Solution
* 用 stack 方式處理

### Code
```python
class Solution:
    def minAddToMakeValid(self, S: "str") -> "int":
        count = 0
        stack = []

        for s in S:
            if s == "(":
                stack.append(s)
                continue
            elif len(stack) == 0:
                count += 1
                continue
            elif stack[-1] == ")":
                count += 1
            stack.pop()
        return count + len(stack)
```

###### tags: `LeetCode` `python` `Minimum Add to Make Parentheses Valid` 