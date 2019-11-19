class Solution:
    def getRow(self, rowIndex: 'int') -> 'List[int]':

        res = [[1], [1, 1]]

        if rowIndex < 2:
            return res[rowIndex]

        i = 2
        while i <= rowIndex:
            temp = [1]
            for index, value in enumerate(res[i - 1]):
                if index != len(res[i - 1])-1:
                    temp.append(value + res[i - 1][index + 1])
            temp.append(1)
            res.append(temp)
            i += 1
        return res[rowIndex]


myClass = Solution()
result = myClass.getRow(3)
print(result)
