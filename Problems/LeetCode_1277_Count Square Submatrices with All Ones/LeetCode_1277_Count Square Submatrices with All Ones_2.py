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


matrix = [
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]
myClass = Solution()
result = myClass.countSquares(matrix)
print(result)
