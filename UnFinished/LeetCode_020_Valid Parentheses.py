class Solution:
    def isValid(self, s: str) -> bool:
        rule = {")":"(","}":"{","]":"["}
        stack = []
        flag = True

        for item in s:
            if item in rule.values():
                stack.append(item)
            else:
                if((len(stack)==0)or(rule[item]!=stack.pop())):
                    flag = False
                    break

        if(len(stack)!=0):
            flag = False
        return flag

myClass = Solution()
result = myClass.isValid("]")
print(result)