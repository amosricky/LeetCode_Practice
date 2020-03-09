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
