# 【LeetCode】 070. Climbing Stairs

## Description
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

## Example1:

```
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
```

## Example2:

```
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
```

## Solution1
* Recursive (Time Out)

### Code1
```python
class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        if n <= 2:
            return n
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)
```

## Solution2
* Dynamic Programming

### Code2
```python
class Solution:
    def climbStairs(self, n: 'int') -> 'int':
        res = [1, 2]
        if n <= 2:
            return res[n-1]

        for i in range(3, n+1):
            val = res[i-3] + res[i-2]
            res.append(val)

        return res[n-1]
```

###### tags: `LeetCode` `python` `Climbing Stairs` 