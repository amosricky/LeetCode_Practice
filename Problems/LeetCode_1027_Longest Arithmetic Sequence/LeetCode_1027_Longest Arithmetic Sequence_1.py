class Solution:
    def longestArithSeqLength(self, A: "List[int]") -> "int":

        tempLists = []

        for num in A:
            appendTempLists = []
            for temp in tempLists:
                if len(temp) > 1:
                    if (temp[1] - temp[0]) == (num - temp[-1]):
                        temp.append(num)
                else:
                    newList = temp + [num]
                    if newList not in tempLists:
                        appendTempLists.append(newList)

            if [num] not in tempLists:
                appendTempLists.append([num])
            tempLists = tempLists + appendTempLists
        tempListsLen = [len(temp) for temp in tempLists]
        return max(tempListsLen)


myClass = Solution()
result = myClass.longestArithSeqLength([20,1,15,3,10,5,8,0])
print(result)
