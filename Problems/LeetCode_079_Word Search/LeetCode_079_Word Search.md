# 【LeetCode】 079. Word Search

## Description
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

## Example:
```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
```

## Solution1
* DFS + Backtracking。
* 首先要從棋盤上選擇一個位置對四周進行搜尋。
* 由於用過的格子不能重複使用，每次在進入 dfs 的時候，必須要記錄是否有造訪(visit)過這個格子，才往更深處呼叫；同時，在該層的四個方向都判斷完以後，回到上一層之前，必須將造訪的紀錄還原回去。
* 在實作時為了方便起見，將搜尋過的值暫時設為"0"，後面再還原，可避免另外儲存走訪紀錄。
### Code1
```python
class Solution:
    def exist(self, board: "List[List[str]]", word: "str") -> "bool":

        for index_Row, _ in enumerate(board):
            for index_Column, _ in enumerate(board[index_Row]):
                chk = self.backTracking([index_Row, index_Column], board, word, 0)
                if chk:
                    return True
        return False

    def backTracking(self, coordinate: "List", board: "List[List[str]]", word: "str", idx: "int") -> "bool":
        row = coordinate[0]
        col = coordinate[1]
        len_row = len(board)
        len_col = len(board[0])

        if board[row][col] != word[idx]:
            return False

        if idx == len(word) - 1:
            return True

        tmp = board[row][col]
        board[row][col] = "0"

        if 0 <= row - 1 < len_row and self.backTracking([row - 1, col], board, word, idx + 1):
            return True
        if 0 <= row + 1 < len_row and self.backTracking([row + 1, col], board, word, idx + 1):
            return True
        if 0 <= col - 1 < len_col and self.backTracking([row, col - 1], board, word, idx + 1):
            return True
        if 0 <= col + 1 < len_col and self.backTracking([row, col + 1], board, word, idx + 1):
            return True

        board[row][col] = tmp
        return False
```

## Solution2
* DFS + Backtracking。
* 之前面試碰到的考題, 為此題之變形, 要求在陣列中找尋字串(且字串方向有一致性), 並需要輸入查詢次數及搜尋字串
### Code2
```python
class Solution:
    def exist(self, board: "List[List[str]]", word: "str") -> "bool":

        for index_Row, _ in enumerate(board):
            for index_Column, _ in enumerate(board[index_Row]):
                # Check up
                if self.backTracking([index_Row, index_Column], board, word, 0, [-1, 0]):
                    return True
                # Check down
                if self.backTracking([index_Row, index_Column], board, word, 0, [1, 0]):
                    return True
                # Check left
                if self.backTracking([index_Row, index_Column], board, word, 0, [0, -1]):
                    return True
                # Check right
                if self.backTracking([index_Row, index_Column], board, word, 0, [0, 1]):
                    return True
        return False

    def backTracking(self, coordinate: "List", board: "List[List[str]]", word: "str", idx: "int", direct: "List[int]") -> "bool":
        row = coordinate[0]
        col = coordinate[1]
        len_row = len(board)
        len_col = len(board[0])

        if board[row][col] != word[idx]:
            return False

        if idx == len(word) - 1:
            return True

        if 0 <= row + direct[0] < len_row and 0 <= col + direct[1] < len_col:
            return self.backTracking([row + direct[0], col + direct[1]], board, word, idx + 1, direct)
        return False


if __name__ == '__main__':

    board = [
         ["A", "B", "C", "E"],
         ["S", "F", "E", "S"],
         ["A", "D", "E", "E"]
    ]

    times = input("Input search times : ")
    for _ in range(int(times)):
        word = input("Search word : ")
        myClass = Solution()
        res = myClass.exist(board, word)
        print(res)
```

###### tags: `LeetCode` `python` `Word Search` 