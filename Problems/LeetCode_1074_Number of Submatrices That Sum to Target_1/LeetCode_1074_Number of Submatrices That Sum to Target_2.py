class Solution:
    def numSubmatrixSumTarget(self, matrix: "List[List[int]]", target: "int") -> "int":

        count = 0
        height = len(matrix)
        weidth = len(matrix[0])

        coordinates = [[i, j] for i in range(height) for j in range(weidth)]

        for coordinate in coordinates:
            subCoordinates = [[i, j] for i in range(coordinate[0], height) for j in range(coordinate[1], weidth)]
            for subCoordinate in subCoordinates:
                if coordinate == subCoordinate and matrix[coordinate[0]][coordinate[1]] == target:
                    count += 1
                    continue
                elif coordinate != subCoordinate:
                    checkResult = self.check(matrix, target, coordinate, subCoordinate[1]-coordinate[1]+1, subCoordinate[0]-coordinate[0]+1)
                    if checkResult:
                        count += 1
        return count

    def check(self, matrix, target, startPoint, weight, height):

        subMatrixSum = 0

        for i in range(0, height):
            subMatrixSum += sum(matrix[startPoint[0] + i][startPoint[1]:startPoint[1] + weight])

        if subMatrixSum == target:
            return True
        return False


myClass = Solution()
result = myClass.numSubmatrixSumTarget([[0, 1, 0], [1, 1, 1], [0, 1, 0]], 0)
print(result)
