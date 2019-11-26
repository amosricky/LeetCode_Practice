# 【LeetCode】 771. Jewels and Stones

## Description
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Note:
+ S and J will consist of letters and have length at most 50.
+ The characters in J are distinct.
## Example:

```
Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3


Example 2:

Input: J = "z", S = "ZZ"
Output: 0
```

## Solution

* 利用 set 特性，取出不同的 jewel。
* 計算 Stone 於 jewel set 的次數。

### Code
```python
class Solution:
    def numJewelsInStones(self, J: 'str', S: 'str') -> 'int':
        targetSet = set(J)
        count = 0

        for target in targetSet:
            count += S.count(target)

        return count
```

###### tags: `LeetCode` `python` `Jewels and Stones` 