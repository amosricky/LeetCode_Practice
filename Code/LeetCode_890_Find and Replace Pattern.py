class Solution:
    def findAndReplacePattern(self, words: 'List[str]', pattern: 'str') -> 'List[str]':
        rule = {}
        res = []

        for word in words:
            check = True
            for index, alpha in enumerate(word):
                if (pattern[index] not in rule.keys()) and (alpha not in rule.values()):
                    rule[pattern[index]] = alpha

                elif (pattern[index] in rule.keys()) and (alpha == rule[pattern[index]]):
                    continue
                else:
                    check = False
                    break

            if check:
                res.append(word)
            rule = {}

        return res


myClass = Solution()
result = myClass.findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc", "aaa"], "zxx")
print(result)
