class Solution:
    def numSubmatrixSumTarget(self, matrix: "List[List[int]]", target: "int") -> "int":

        count = 0
        repeat = 0
        single = 0
        height = len(matrix)
        weidth = len(matrix[0])

        coordinates = [[i, j] for i in range(height) for j in range(weidth)]

        for i in range(1, len(coordinates)):
            for j in range(0, i):
                nodeA = coordinates[i]
                nodeB = coordinates[j]
                leftTop = [min(nodeA[0], nodeB[0]), min(nodeA[1], nodeB[1])]
                subWeight = abs(nodeA[1] - nodeB[1]) + 1
                subHeight = abs(nodeA[0] - nodeB[0]) + 1
                checkResult = self.check(matrix, target, leftTop, subWeight, subHeight)
                if checkResult:
                    count += 1
                if checkResult and subWeight > 1 and subHeight > 1:
                    repeat += 1

        for coordinate in coordinates:
            if matrix[coordinate[0]][coordinate[1]] == target:
                single += 1

        return count - int(repeat / 2) + single

    def check(self, matrix, target, startPoint, weight, height):

        subMatrixSum = 0

        for i in range(0, height):
            subMatrixSum += sum(matrix[startPoint[0] + i][startPoint[1]:startPoint[1] + weight])
        if subMatrixSum == target:
            return True
        return False