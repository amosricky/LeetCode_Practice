class Solution:
    def combinationSum2(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        if not target:
            return []
        self.res = []
        candidates.sort()
        self.find(candidates, target, [])
        return self.res

    def find(self, remainingCandidates: 'List[int]', target: 'int', tempANS: 'List[int]'):

        for index, value in enumerate(remainingCandidates):
            if value < target and index < len(remainingCandidates) - 1:
                self.find(remainingCandidates[index + 1:], target - value, tempANS + [value])
                continue
            elif value == target:
                if not (tempANS + [value]) in self.res:
                    self.res.append(tempANS + [value])
                return
            return


myClass = Solution()
result = myClass.combinationSum2([10,1,2,7,6,1,5], 8)
print(result)
