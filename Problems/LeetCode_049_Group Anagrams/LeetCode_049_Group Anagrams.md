# 【LeetCode】 049. Group Anagrams

## Description
Given an array of strings, group anagrams together.

Note:

+ All inputs will be in lowercase.
+ The order of your output does not matter.
## Example:

```
Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
```

## Solution1
* 先將值 sort 後建成 hash map 的 key，接著依序將值塞入 map 即可求解。

### Code1
```python
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
```
## Solution2
* 也可用字母比對的方式，相同的 Anagrams 用的字母會一樣。

![](https://leetcode.com/problems/group-anagrams/Figures/49_groupanagrams2.png)

###### tags: `LeetCode` `python` `Group Anagrams` 