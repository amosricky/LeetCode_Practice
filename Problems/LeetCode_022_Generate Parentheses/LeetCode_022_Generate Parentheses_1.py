class Solution:
    def __init__(self):
        self.res = []

    def generateParenthesis(self, n: 'int') -> 'List[str]':
        self.add("", n)
        return self.res

    def add(self, tmp: 'str', n: 'int'):
        if len(tmp) == n*2 and tmp.count("(") == tmp.count(")") == n:
            self.res.append(tmp)
        else:
            L = tmp.count("(")
            R = tmp.count(")")

            if L >= R + 1 and R + 1 <= n:
                self.add(tmp + ")", n)
            if L + 1 >= R and L + 1 <= n:
                self.add(tmp + "(", n)


myClass = Solution()
result = myClass.generateParenthesis(3)
print(result)
