# 【LeetCode】 1074. Number of Submatrices That Sum to Target

## Description
Given a matrix, and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate that is different: for example, if x1 != x1'.

Note:
+ 1 <= matrix.length <= 300
+ 1 <= matrix[0].length <= 300
+ -1000 <= matrix[i] <= 1000
+ -10^8 <= target <= 10^8

## Example 1:
```
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
```

## Example 2:
```
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
```

## Solution1
[Time Out]
* 取區任意 2 點座標可得到 1 submatrix。
* 判斷 submatrix 的 Sum 是否等於 K 。
* 但若 submatrix 邊界 > 1 會重複取到同一個 submatrix , 所以最後需扣掉。
* 加上 single node。

### Code1
```python
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
```
## Solution2
[Time Out]
* 簡化一下 solution1 作法, 取到第一個點後 , 只往右/下取第二個點 , 可避免重複問題。

### Code2
```python
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
```
## Solution3
[Time Out]
* 參考 LeetCode 上大神的作法改寫。
* 由上而下, 將每個 row 往下累加, 可得到一維 list, 在找其中是否有 subList 的 sum 為 k。
(計算 subarraySum 需在精進)
```
ex. matrix = 
[[0, 1, 0], 
[1, 1, 1], 
[0, 1, 0]]

row = 0
list = [0, 1, 0] // row[0] 
list = [1, 2, 1] // row[0]+row[1]
list = [1, 3, 1] // row[0]+row[1]+row[2]

row = 1
list = [1, 1, 1] // row[1]
list = [1, 2, 1] // row[1]+row[2]

row = 2
list = [0, 1, 0] // row[2]
```

### Code3
```python
class Solution:
    def numSubmatrixSumTarget(self, matrix: "List[List[int]]", target: "int") -> "int":
        m = len(matrix)
        n = len(matrix[0])
        count = 0
        for i in range(m):
            nums = [0] * n
            for j in range(i, m):
                for k in range(n):
                    nums[k] += matrix[j][k]
                count += self.subarraySum(nums, target)
        return count

    def subarraySum(self, nums: "List[int]", k: "int") -> "int":
        sumList = []
        total = 0
        count = 0

        for index, num in enumerate(nums):
            total += num
            want = total - k
            if want == 0:
                count += 1
                count += sumList.count(0)
            else:
                count += sumList.count(want)
            sumList.append(total)
        return count
```
## Solution4
[效能極佳]
* LeetCode 上大神的作法, solution 3 方式一樣。
* 主要差在 subarraySum 計算方式。

### Code4
```python
class Solution:
    def numSubmatrixSumTarget(self, matrix: "List[List[int]]", target: "int") -> "int":
        m = len(matrix)
        n = len(matrix[0])
        count = 0
        for i in range(m):
            nums = [0] * n
            for j in range(i, m):
                for k in range(n):
                    nums[k] += matrix[j][k]
                count += self.subarraySum(nums, target)
                print(nums)
                print(self.subarraySum(nums, target))
        return count

    def subarraySum(self, nums: "List[int]", k: "int") -> "int":
        freq_map = {0: 1}
        result = 0
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum - k in freq_map:
                result += freq_map[curr_sum - k]
            freq_map[curr_sum] = freq_map.get(curr_sum, 0) + 1
        return result
```

###### tags: `LeetCode` `python` `Number of Submatrices That Sum to Target` 