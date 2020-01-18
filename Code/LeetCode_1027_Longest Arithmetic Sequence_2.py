class Solution:
    def longestArithSeqLength(self, A) -> int:
        diffRecord = [{}]*len(A)
        result = 0
        for endPoint in range(0, len(A)):
            for startPoint in range(0, endPoint):
                diff = A[endPoint] - A[startPoint]
                if diff in diffRecord[startPoint]:
                    diffRecord[endPoint][diff] = diffRecord[startPoint][diff]+1
                else:
                    diffRecord[endPoint][diff] = 2
                result = max(result, diffRecord[endPoint][diff])

        return result



myClass = Solution()
result = myClass.longestArithSeqLength([20,1,15,3,10,5,8,0])
print(result)
