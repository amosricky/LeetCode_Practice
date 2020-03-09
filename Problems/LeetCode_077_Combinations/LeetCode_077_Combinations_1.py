class Solution:
    def __init__(self):
        self.res = []

    def combine(self, n: "int", k: "int") -> "List[List[int]]":
        self.find(1, n, [], k)
        return self.res


    def find(self, start, n, tempAns, k):
        if len(tempAns) == k:
            self.res.append(tempAns)
        else:
            for i in range(start, n+1):
                self.find(i+1, n, tempAns+[i], k)


myClass = Solution()
result = myClass.combine(4, 2)
print(result)
