class Solution:
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        if n == 0:
            return []
        parenthesisLists = ["("]
        start = 2
        while start <= 2 * n:
            tempParenthesisLists = []
            for parenthesisList in parenthesisLists:
                if parenthesisList.count("(") < n:
                    tempAppendLeft = parenthesisList + "("
                    if self.isLegal(tempAppendLeft):
                        tempParenthesisLists.append(tempAppendLeft)
                if parenthesisList.count(")") < n:
                    tempAppendRight = parenthesisList + ")"
                    if self.isLegal(tempAppendRight):
                        tempParenthesisLists.append(tempAppendRight)
            parenthesisLists = tempParenthesisLists
            start += 1
        return parenthesisLists

    def isLegal(self, target: 'List[str]') -> 'bool':
        countLeft = target.count("(")
        countRight = target.count(")")
        return countLeft >= countRight


myClass = Solution()
result = myClass.generateParenthesis(3)
print(result)
