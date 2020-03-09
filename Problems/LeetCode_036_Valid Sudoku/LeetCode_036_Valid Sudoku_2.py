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


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
myClass = Solution()
result = myClass.isValidSudoku(board)
print(result)
