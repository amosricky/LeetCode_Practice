class Solution:
    def mctFromLeafValues(self, arr: "List[int]") -> "int":
        res = 0
        while len(arr) > 1:
            minIndex = arr.index(min(arr))
            if 0 < minIndex < len(arr) - 1:
                res += min(arr[minIndex - 1], arr[minIndex + 1]) * arr[minIndex]
            else:
                res += arr[1 if minIndex == 0 else minIndex - 1] * arr[minIndex]
            arr.pop(minIndex)
        return res


myClass = Solution()
result = myClass.mctFromLeafValues([6, 3, 2, 1])
print(result)
