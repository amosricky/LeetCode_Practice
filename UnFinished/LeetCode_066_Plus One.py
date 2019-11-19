class Solution:
    def plusOne(self, digits: 'List[int]') -> 'List[int]':
        num = ''
        while len(digits)!=0 :
            num += str(digits.pop(0))
        num = int(num)
        num += 1
        return list(str(num))

myClass = Solution()
result = myClass.plusOne([4,3,2,1])
print(result)
