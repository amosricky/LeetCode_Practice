# 【LeetCode】 392. Is Subsequence

## Description
Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Follow up:

+ If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

## Example 1:
```
s = "abc", t = "ahbgdc"
Return true.
```

## Example 2:
```
s = "axc", t = "ahbgdc"
Return false.
```

## Solution1
* Dynamic Programming
* 以 last 紀錄上次結尾, 取出 sub string 動態搜尋

### Code1
```python
class Solution:
    def isSubsequence(self, s: "str", t: "str") -> "bool":

        last = 0
        for char in s:
            if char in t[last:]:
                last = t[last:].index(char) + last + 1
            else:
                return False
        return True
```

## Solution2
* Greedy

### Code2
```python
class Solution:
    def isSubsequence(self, s: "str", t: "str") -> "bool":

        s_len, t_len = len(s), len(t)
        i, j = 0, 0

        while i < s_len and j < t_len:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == s_len
```

## Solution3
* Binary Search
* 先以 record 紀錄 t 中所有 char 的 index, 再取 s 中的 char 與 record 中對應的 index list 進行 binary search

### Code3
```python
class Solution:
    def isSubsequence(self, s: "str", t: "str") -> "bool":

        pre = -1
        record = {}
        for index, value in enumerate(t):
            if value not in record.keys():
                record[value] = [index]
            else:
                record[value].append(index)

        for char in s:
            if char not in record.keys():
                return False
            pre = self.binarySearch(record[char], pre)

            if pre == -1:
                return False

            pre += 1

        return True

    def binarySearch(self, recordList: "list", target: "int") -> "int":

        left, right = 0, len(recordList)-1

        while left < right:
            mid = (left + right) // 2
            if recordList[mid] < target:
                left = mid + 1
            else:
                right = mid

        if recordList[left] < target:
            return -1

        return recordList[left]
```

###### tags: `LeetCode` `python` `Is Subsequence` 