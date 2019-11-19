class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        targetSet = set(J)
        count = 0

        for target in targetSet:
            count += S.count(target)

        return count


myClass = Solution()
result = myClass.numJewelsInStones("aA", "aAAbbbb")
print(result)