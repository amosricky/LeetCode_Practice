# 【LeetCode】 338. Counting Bits

## Description
Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Follow up:
+ It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
+ Space complexity should be O(n).
+ Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
## Example:

```
Example 1:

Input: 2
Output: [0,1,1]


Example 2:

Input: 5
Output: [0,1,1,2,1,2]
```

## Solution1

* 轉成 2 進制後在轉為字串 ， count 為 "1" 之數目。
* 但時間複雜度為 O(n*sizeof(integer))。

### Code1
```python
class Solution:
    def countBits(self, num: 'int') -> 'List[int]':
        res = []
        for n in range(num+1):
            nStr = bin(n)
            res.append(nStr.count("1"))
        return res
```
## Solution2

* 偶數 n 轉為 2 進制後結為必為 0 , 故 "1" 的數量必與 n/2 一樣"。 ex. 30 => bin(11110) , 30/2 = 15 => bin(1111)。 
* 基數 n 轉為 2 進制後結尾必為 1 , 故取 (n-1)/2 再加 1。

### Code2
```python
class Solution:
    def countBits(self, num: 'int') -> 'List[int]':
        res = [0] * (num + 1)
        for n in range(1, num + 1):
            if n % 2 == 0:
                res[n] = res[n//2]
            else:
                res[n] = int(res[(n-1)//2])+1
        return res
```

###### tags: `LeetCode` `python` `Counting Bits` 