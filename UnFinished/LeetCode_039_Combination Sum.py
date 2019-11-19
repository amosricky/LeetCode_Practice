class Solution:
    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        res = []

        for candidate in candidates:
            tempCombination = []
            if candidate <= target:
                tempCombination.append(candidate)
                res.append(tempCombination)

        if not res:
            return res

        while not self.checkSum(res, target):
            tempRes = []
            for checkList in res:
                if sum(checkList) == target:
                    tempRes.append(checkList)
                else:
                    for candidate in candidates:
                        tempList = checkList + [candidate]
                        if sum(tempList) <= target and self.checkDuplicate(tempRes, tempList):
                            tempRes.append(tempList)
            res = tempRes

        return res

    def checkSum(self, checkSumLists: 'List[List[int]]', target: 'int') -> 'bool':
        res = True
        for checkList in checkSumLists:
            if sum(checkList) != target:
                res = False
                return res
        return res

    def checkDuplicate(self, checkDuplicateLists: 'List[List[int]]', targetList: '[List[int]') -> 'bool':
        res = True
        targetList.sort()
        for checkDuplicateList in checkDuplicateLists:
            checkDuplicateList.sort()
            if targetList == checkDuplicateList:
                res = False
                return res
        return res


myClass = Solution()
result = myClass.combinationSum([2, 3, 5], 8)
print(result)
