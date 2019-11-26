# 【LeetCode】 48. Rotate Image

## Description
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
+ You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
+ DO NOT allocate another 2D matrix and do the rotation.

## Example:

```
Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]


Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```

## Solution1

* 先得出由外而內需轉動的圈數。
* 因為規定使用in-place，所以每次旋轉四個數值。

### Code
```python
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
```

## Solution2

* 以鏡像操作的方式先上下列互換。
* 再左下右上互換。

### Code
```python
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
```

###### tags: `LeetCode` `python` `Rotate Image` 