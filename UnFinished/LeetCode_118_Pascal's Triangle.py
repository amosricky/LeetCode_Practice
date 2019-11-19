class Solution:
    def generate(self, numRows: 'int') -> 'List[List[int]]':

        if not numRows:
            return []

        if numRows == 1:
            return [[1]]

        if numRows == 2:
            return [[1], [1, 1]]
        res = [[1], [1, 1]]
        i = 3
        while i <= numRows:
            temp = [1]
            for index, value in enumerate(res[i - 2]):
                if index != len(res[i - 2])-1:
                    temp.append(value + res[i - 2][index + 1])
            temp.append(1)
            res.append(temp)
            i += 1
        return res


myClass = Solution()
result = myClass.generate(5)
print(result)
