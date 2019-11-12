class Solution:
    def isPalindrome(self, x: int) -> bool:

        if(x<0): return False

        target = x
        revert = 0

        while(target!=0):
            tail = target%10
            revert = revert*10+tail
            target = int(target/10)

        if(revert == x):
            return True
        else:
            return False

myClass = Solution()
reverseResult = myClass.isPalindrome(-12321)
print(reverseResult)