class Solution:
    def __init__(self):
        self.res = []

    def combinationSum2(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        if not target:
            return []
        candidates.sort()
        self.find(candidates, target, [])
        return self.res

    def find(self, remaining: 'List[int]', target: 'int', tempANS: 'List[int]'):

        for index, value in enumerate(remaining):
            if value < target and index < len(remaining) - 1:
                self.find(remaining[index + 1:], target - value, tempANS + [value])
                continue
            elif value == target:
                if not (tempANS + [value]) in self.res:
                    self.res.append(tempANS + [value])
                return
            return


myClass = Solution()
result = myClass.combinationSum2([2, 5, 2, 1, 2], 5)
print(result)
