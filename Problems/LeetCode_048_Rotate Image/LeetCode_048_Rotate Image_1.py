class Solution:
    def rotate(self, matrix: 'List[List[int]]') -> 'None':
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowsMaxIndex = len(matrix) - 1
        columnsMaxIndex = len(matrix[0]) - 1
        times = round(len(matrix) / 2)

        for time in range(0, times):
            for index, temp in enumerate(matrix[time][time:columnsMaxIndex - time]):
                matrix[time][index + time] = matrix[rowsMaxIndex - index - time][time]
                matrix[rowsMaxIndex - index - time][time] = matrix[rowsMaxIndex - time][rowsMaxIndex - time - index]
                matrix[rowsMaxIndex - time][rowsMaxIndex - time - index] = matrix[index + time][columnsMaxIndex - time]
                matrix[index + time][columnsMaxIndex - time] = temp

                # print(temp)
                # print(matrix[time][index + time])
                # print(matrix[rowsMaxIndex - index - time][time])
                # print(matrix[rowsMaxIndex - time][rowsMaxIndex - time - index])
                # print(matrix[index + time][columnsMaxIndex - time])


matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]
myClass = Solution()
myClass.rotate(matrix)
