class Solution:
    def lengthOfLastWord(self, s: 'str') -> 'int':
        strList = s.split(" ")

        while len(strList) > 0:
            str = strList.pop()
            if str:
                return len(str)
        return 0


myClass = Solution()
result = myClass.lengthOfLastWord("a ")
print(result)
