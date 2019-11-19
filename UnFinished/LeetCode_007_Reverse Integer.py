class Solution:
    def reverse(self, x: int) -> int:

        if x >= 2 ** 31 - 1 or x <= -2 ** 31: return 0

        result = 0
        tempValue = abs(x)
        flag = 1 if (x>=0) else -1

        while(tempValue!=0):
            tail = tempValue%10
            result = result*10+tail
            tempValue = int(tempValue/10)

        result = flag*result

        if (result >= 2 ** 31 - 1 or result <= -2 ** 31):
            return 0
        else:
            return result

myClass = Solution()
reverseResult = myClass.reverse(1534236469)
print(reverseResult)
