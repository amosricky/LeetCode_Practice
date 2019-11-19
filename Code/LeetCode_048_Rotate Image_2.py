class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        for addValue in range(len(matrix)//2):
            tempList = matrix[0 + addValue]
            matrix[0 + addValue] = matrix[-1-addValue]
            matrix[-1 - addValue] = tempList

        for row in range(0, len(matrix)-1):
            for column in range(row + 1, len(matrix[0])):
                temp = matrix[row][column]
                matrix[row][column] = matrix[column][row]
                matrix[column][row] = temp

        print(matrix)


matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
myClass = Solution()
myClass.rotate(matrix)
