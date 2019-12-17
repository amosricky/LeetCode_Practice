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


matrix = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
myClass = Solution()
result = myClass.countSquares(matrix)
print(result)
