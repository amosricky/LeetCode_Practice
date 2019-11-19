class Solution:
    def strStr(self, haystack: 'str', needle: 'str') -> 'int':
        if haystack == needle:
            return 0
        for i in range(0, (len(haystack) - len(needle)+1)):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


myClass = Solution()
result = myClass.strStr("hello", "ll")
print(result)
