# 【LeetCode】 1277. Count Square Submatrices with All Ones

## Description
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

Constraints:

+ 1 <= arr.length <= 300
+ 1 <= arr[0].length <= 300
+ 0 <= arr[i][j] <= 1

## Example 1:
```
Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
```

## Example 2:
```
Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
```

## Solution1
* 暴力法，edge 為欲找尋 square 之邊長。
* 不同 square 對應不同起點範圍。
```
假設 matrix = [
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

找尋 1*1 時，須以所有座標點為起點搜尋,
但找尋 2*2 時，以不為 N 支座標點向右下拓展 2*2 square 檢查是否滿足需求
[
  [0,1,1,N],
  [1,1,1,N],
  [N,N,N,N]
]

找尋 3*3 時 
[
  [0,1,N,N],
  [N,N,N,N],
  [N,N,N,N]
]
```

### Code1
```python
class Solution:
    def countSquares(self, matrix: "List[List[int]]") -> "int":
        columns = len(matrix[0])
        rows = len(matrix)
        shortSide = min(columns, rows)
        edge = 1
        res = 0

        while edge <= shortSide:
            for row in range(0, rows - edge + 1):
                for column in range(0, columns - edge + 1):
                    if not matrix[row][column]:
                        continue
                    find = True
                    for i in range(row, row + edge):
                        if 0 in matrix[i][column:column + edge]:
                            find = False
                            break
                    if find:
                        res += 1
            edge += 1
        return res
```
## Solution2
![](https://leetcode.jp/wp-content/uploads/2019/12/1-2.png)
* 參考上圖方法 [原文](https://leetcode.jp/leetcode-1277-count-square-submatrices-with-all-ones-%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF%E5%88%86%E6%9E%90/)
* 以動態規劃方式以每個座標點為起點，向左上方拓展找到最大 square (與圖例方向相反)。
* p.s. 若能找到 3*3，代表該點可同時滿足 2*2、1*1，故 result += 3

### Code2
```python
class Solution:
    def countSquares(self, matrix: "List[List[int]]") -> "int":
        columns = len(matrix[0])
        rows = len(matrix)
        res = 0

        for row in range(0, rows):
            for column in range(0, columns):
                if row and column and matrix[row][column]:
                    matrix[row][column] = min(matrix[row-1][column], matrix[row][column-1], matrix[row-1][column-1]) + 1
                res += matrix[row][column]
        return res
```

###### tags: `LeetCode` `python` `Count Square Submatrices with All Ones` 