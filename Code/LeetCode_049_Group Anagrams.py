class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        res = []
        dict = {}

        for item in strs:
            itemStr = sorted(list(item))
            itemitemStr = "".join(itemStr)
            if itemitemStr in dict:
                dict[itemitemStr].append(item)
            else:
                dict[itemitemStr] = [item]

        for value in dict.values():
            res.append(value)

        return res


myClass = Solution()
result = myClass.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(result)
