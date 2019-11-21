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


board = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."]
]
myClass = Solution()
result = myClass.isValidSudoku(board)
print(result)
