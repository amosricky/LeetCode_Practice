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


board = [
     ["A", "B", "C", "E"],
     ["S", "F", "E", "S"],
     ["A", "D", "E", "E"]
]

word = "ABCESEEEFS"

myClass = Solution()
res = myClass.exist(board, word)
print(res)
