class Solution:
    def __init__(self):
        self.res = []

    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        candidates.sort()
        self.find(candidates, 0, target, [])
        return self.res

    def find(self, candidates, start, target, tempAns):
        if target == 0:
            self.res.append(tempAns)
        elif target < candidates[0]:
            return
        else:
            for i in range(start, len(candidates)):
                self.find(candidates, i, target - candidates[i], tempAns + [candidates[i]])


myClass = Solution()
result = myClass.combinationSum([2, 3, 5], 8)
print(result)
