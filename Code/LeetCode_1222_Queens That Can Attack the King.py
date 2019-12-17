class Solution:
    def queensAttacktheKing(self, queens: "List[List[int]]", king: "List[int]") -> "List[List[int]]":
        directionList = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        res = []

        for direction in directionList:
            newLocation = [sum(i) for i in zip(king, direction)]
            while 8 > newLocation[0] > -1 and 8 > newLocation[1] > -1:
                if newLocation in queens:
                    res.append(newLocation)
                    break
                newLocation = [sum(i) for i in zip(newLocation, direction)]

        return res


king = [3,4]
queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]]
myClass = Solution()
result = myClass.queensAttacktheKing(queens, king)
print(result)
