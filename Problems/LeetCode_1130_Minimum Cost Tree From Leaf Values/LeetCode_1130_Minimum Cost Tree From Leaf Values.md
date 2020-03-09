# 【LeetCode】 1130. Minimum Cost Tree From Leaf Values

## Description
Given an array arr of positive integers, consider all binary trees such that:

+ Each node has either 0 or 2 children;
+ The values of arr correspond to the values of each leaf in an in-order traversal of the tree.  (Recall that a node is a leaf if and only if it has 0 children.)
+ The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree respectively.

Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node.  It is guaranteed this sum fits into a 32-bit integer.

Note:
+ 2 <= arr.length <= 40
+ 1 <= arr[i] <= 15
+ It is guaranteed that the answer fits into a 32-bit signed integer (ie. it is less than 2^31).

## Example 1:
```
Input: arr = [6,2,4]
Output: 32
Explanation:
There are two possible trees.  The first has non-leaf node sum 36, and the second has non-leaf node sum 32.

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4
```

## Solution1
![](https://imgur.com/60HtKth.png)

參考 [影片](https://www.youtube.com/watch?v=xcYkzSrgOmY)
* Greedy 作法 , 每次都先從 arr stack 取最小值然後與較小的鄰點做乘積。
* 若最小值 index 剛好為 0 則取 arr[1], 若最小值 index 為 stack 尾巴, 則向前取。
* 每加上一次乘積 pop 掉該 minIndex。

### Code1
```python
class Solution:
    def mctFromLeafValues(self, arr: "List[int]") -> "int":
        res = 0
        while len(arr) > 1:
            minIndex = arr.index(min(arr))
            if 0 < minIndex < len(arr) - 1:
                res += min(arr[minIndex - 1], arr[minIndex + 1]) * arr[minIndex]
            else:
                res += arr[1 if minIndex == 0 else minIndex - 1] * arr[minIndex]
            arr.pop(minIndex)
        return res
```
## Solution2
參考 [原文](https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/340004/Python-Easy-DP)
* DP 作法 - max(arr[i]..arr[k]) * max(arr[k+1]..arr[j]) + dp(i, k) + dp(k+1, j).。

### Code2
```python
class Solution:
    def mctFromLeafValues(self, arr: "List[int]") -> "int":
        self.memo = {}

        def dp(i, j):
            if j <= i:
                return 0
            if (i, j) not in self.memo:
                res = float('inf')
                for k in range(i + 1, j + 1):
                    res = min(dp(i, k - 1) + dp(k, j) + max(arr[i:k]) * max(arr[k:j + 1]), res)
                self.memo[(i, j)] = res
            return self.memo[(i, j)]

        return dp(0, len(arr) - 1)
```
###### tags: `LeetCode` `python` `Minimum Cost Tree From Leaf Values` 