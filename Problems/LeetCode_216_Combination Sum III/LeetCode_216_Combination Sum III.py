class Solution:
    def __init__(self):
        self.res = []

    def combinationSum3(self, k: "int", n: "int") -> "List[List[int]]":
        self.find(1, k, n, [])
        return self.res

    def find(self, start, k, n, tempAns):
        if k == 0 and n == 0:
            self.res.append(tempAns)
            return
        elif n < 0 or k < 0:
            return

        for i in range(start, 10):
            self.find(i + 1, k - 1, n - i, tempAns + [i])


myClass = Solution()
result = myClass.combinationSum3(3, 7)
print(result)
