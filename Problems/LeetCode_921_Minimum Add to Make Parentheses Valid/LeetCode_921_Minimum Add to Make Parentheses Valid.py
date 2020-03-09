class Solution:
    def minAddToMakeValid(self, S: "str") -> "int":
        count = 0
        stack = []

        for s in S:
            if s == "(":
                stack.append(s)
                continue
            elif len(stack) == 0:
                count += 1
                continue
            elif stack[-1] == ")":
                count += 1
            stack.pop()
        return count + len(stack)


myClass = Solution()
result = myClass.minAddToMakeValid("()))((")
print(result)
