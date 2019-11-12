class Solution:
    def isPalindrome(self, s: 'str') -> 'bool':
        cleanList = []
        for str in list(s):
            if str.isalnum():
                cleanList.append(str.upper())
        print(cleanList)
        return cleanList == cleanList[::-1]


myClass = Solution()
result = myClass.isPalindrome("race a car")
print(result)

