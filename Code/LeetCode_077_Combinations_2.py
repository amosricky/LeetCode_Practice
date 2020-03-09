class Solution:
    def __init__(self):
        self.res = []

    def combine(self, n: "int", k: "int") -> "List[List[int]]":
        num = [i for i in range(1, n+1)]
        self.backTracking(num, k, [], 0)
        return self.res

    def backTracking(self, num: "List[int]", k: "int", tmp: "List[int]", idx: "int"):
        if len(tmp) == k:
            self.res.append(tmp.copy())
        elif (idx + 1) <= len(num):
            self.backTracking(num, k, tmp, idx + 1)
            self.backTracking(num, k, tmp + [num[idx]], idx + 1)


myClass = Solution()
result = myClass.combine(4, 2)
print(result)
