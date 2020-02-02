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


island = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
          [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
myClass = Solution()
result = myClass.maxAreaOfIsland(island)
print(result)
