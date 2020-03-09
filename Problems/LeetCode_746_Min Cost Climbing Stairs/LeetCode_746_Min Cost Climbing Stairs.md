# 【LeetCode】 746. Min Cost Climbing Stairs

## Description
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).

Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Note:

+ cost will have a length in the range [2, 1000].
+ Every cost[i] will be an integer in the range [0, 999].

## Example 1:
```
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
```

## Example 2:
```
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
```

## Solution
* [Hint] Say f[i] is the final cost to climb to the top from step i. Then f[i] = cost[i] + min(f[i+1], f[i+2]).
* minCost 依序紀錄到達 i 所需最小 cost, 從最後 2 個選出最小值返回

### Code
```python
class Solution:
    def minCostClimbingStairs(self, cost):
        minCost = []
        minCost.append(cost[0])
        minCost.append(cost[1])

        for i in range(2, len(cost)):
            value = min(minCost[i-1], minCost[i-2]) + cost[i]
            minCost.append(value)
        return min(minCost[-1], minCost[-2])
```

###### tags: `LeetCode` `python` `Min Cost Climbing Stairs` 