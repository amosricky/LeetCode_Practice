class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':

        result = ""
        if (strs==None) or (len(strs)==0):
            return result
        target = strs[0]
        for item in strs:
            if (len(target) > len(item)):
                target = item
        targetLength = len(target)

        while (targetLength != 0):
            slice = target[0:targetLength]
            findResult = self.findPrefix(slice, targetLength, strs)
            if (findResult):
                return slice
            targetLength -= 1
        return result

    def findPrefix(self, slice: 'str', targetLength: 'int', strs: 'List[str]') -> 'bool':
        for item in strs:
            if ((slice != item[0:targetLength])):
                return False
        return True


myClass = Solution()
result = myClass.longestCommonPrefix(["ca","a"])
print(result)