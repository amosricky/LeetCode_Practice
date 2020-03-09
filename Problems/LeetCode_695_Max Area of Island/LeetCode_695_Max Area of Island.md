# 【LeetCode】 695. Max Area of Island

## Description
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Note:

+ The length of each dimension in the given grid does not exceed 50.

## Example 1:
```
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.
```

## Example 2:
```
[[0,0,0,0,0,0,0,0]]

Given the above grid, return 0.
```

## Solution
* 以 DFS 方式搜尋。
* 搜尋過的節點改為 0 (grid[point_i][point_j] = 0), 避免重複計算。

### Code
```python
class Solution:
    def maxAreaOfIsland(self, grid: "List[List[int]]") -> "int":
        lenWidth = len(grid[0])
        lenHeight = len(grid)
        maxArea = 0

        def check(point_i, point_j):
            if (0 <= point_i < lenHeight) and (0 <= point_j < lenWidth) and grid[point_i][point_j]:
                grid[point_i][point_j] = 0
                return check(point_i + 1, point_j) + check(point_i - 1, point_j) + check(point_i, point_j + 1) + check(point_i, point_j - 1) + 1
            return 0

        for i in range(lenHeight):
            for j in range(lenWidth):
                if grid[i][j]:
                    area = check(i, j)
                    maxArea = max(maxArea, area)
        return maxArea
```

###### tags: `LeetCode` `python` `Max Area of Island` 