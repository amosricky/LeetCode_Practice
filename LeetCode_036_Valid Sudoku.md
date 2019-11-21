# 【LeetCode】 036. Valid Sudoku

## Description
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

+ Each row must contain the digits 1-9 without repetition.
+ Each column must contain the digits 1-9 without repetition.
+ Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

A partially filled sudoku which is valid.

Note:

+ The number of nodes in the tree is at most 10000.
+ The final answer is guaranteed to be less than 2^31.
## Example:

```
Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true


Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
```

## Solution1
* 共進行 9 次搜尋。
* 每次搜尋分別確認 row , column , square 是否有重複。

### Code1
```python
class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':

        res = True
        for index in range(0, len(board)):
            res = self.check(board[index])
            if not res:
                return res

            res = self.check([column[index] for column in board])
            if not res:
                return res

            rowStart = index // 3 * 3
            square = [row[index % 3 * 3:index % 3 * 3 + 3] for row in board[rowStart:rowStart + 3]]
            squareList = [item for subList in square for item in subList]
            res = self.check(squareList)
            if not res:
                return res
        return res

    def check(self, checkList: 'List[str]'):
        checked = []
        checkRes = True
        for item in checkList:
            if item == '.':
                continue
            if item not in checked:
                checked.append(item)
            else:
                checkRes = False
                return checkRes
        return checkRes
```
## Solution2
* 記錄所有出現過的 row , column , square 的數字及相應位置。
* 最后利用 set 判断是否有重复。

### Code2
```python
class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':

        check = []
        for row in range(len(board)):
            for column in range(len(board)):
                if board[row][column] != '.':
                    check.append(("row", row, board[row][column]))
                    check.append(("column", row, board[row][column]))
                    check.append((row//3, column//3, board[row][column]))
        temp = []
        for i in check:
            if i not in temp:
                temp.append(i)
            
        return len(check) == len(set(check))
```

###### tags: `LeetCode` `python` `Valid Sudoku` 