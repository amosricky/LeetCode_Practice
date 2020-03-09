# 【LeetCode】 1027. Longest Arithmetic Sequence

## Description
Given an array A of integers, return the length of the longest arithmetic subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).

Note:

+ 2 <= A.length <= 2000
+ 0 <= A[i] <= 10000

## Example 1:
```
Input: [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.
```

## Example 2:
```
Input: [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].
```

## Example 3:
```
Input: [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].
```

## Solution1
* 暴力法，算出所有等差數列後求最長。

### Code1
```python
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
```
## Solution2
* DP 作法
* 在 A 的每個位置，以 dictionary 紀錄以當前位置為 endPoint，各種差值的等差數列個數。(key 表示差值，value 表示等差數列的個數)
* 當有後續的 A[endPoint] 減去當前的 A[startPoint] 的差值(diff)在 diffRecord[startPoint][diff] 中時，那麼在 diffRecord[endPoint] 位置，diff 對應的個數加 1 就可以了。

### Code2
```python
class Solution:
    def longestArithSeqLength(self, A) -> int:
        diffRecord = [{}]*len(A)
        result = 0
        for endPoint in range(0, len(A)):
            for startPoint in range(0, endPoint):
                diff = A[endPoint] - A[startPoint]
                if diff in diffRecord[startPoint]:
                    diffRecord[endPoint][diff] = diffRecord[startPoint][diff]+1
                else:
                    diffRecord[endPoint][diff] = 2
                result = max(result, diffRecord[endPoint][diff])

        return result
```

###### tags: `LeetCode` `python` `Longest Arithmetic Sequence` 