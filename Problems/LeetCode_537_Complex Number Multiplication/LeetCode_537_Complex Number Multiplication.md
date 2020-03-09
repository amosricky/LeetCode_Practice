# 【LeetCode】 537. Complex Number Multiplication

## Description
Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

Note:

+ The input strings will not have extra blank.
+ The input strings will be given in the form of a+bi, where the integer a and b will both belong to the range of [-100, 100]. And the output should be also in this form.

## Example 1:
```
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
```

## Example 2:
```
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
```

## Solution1
* 以 regular expression 找出係數後相乘。

### Code1
```python
import re
class Solution:
    def complexNumberMultiply(self, a: "str", b: "str") -> "str":
        strAInts = re.findall(r'-?[0-9]+', a)
        strAIntA = int(strAInts[0])
        strAIntB = int(strAInts[1])

        strBInts = re.findall(r'-?[0-9]+', b)
        strBIntA = int(strBInts[0])
        strBIntB = int(strBInts[1])

        r1 = strAIntA * strBIntA - strAIntB * strBIntB
        r2 = strAIntB * strBIntA + strAIntA * strBIntB

        result = '{r1}+{r2}i'.format(r1=r1, r2=r2)
        return result
```

## Solution2
* golang version

### Code2
```golang
import (
	"fmt"
	"regexp"
	"strconv"
)

func complexNumberMultiply(a string, b string) string {
	regRule := regexp.MustCompile(`-?[0-9]+`)
	strIntA := regRule.FindAllString(a, -1)
	strIntB := regRule.FindAllString(b, -1)
	aR1 , _ := strconv.Atoi(strIntA[0])
	aR2 , _ := strconv.Atoi(strIntA[1])
	bR1 , _ := strconv.Atoi(strIntB[0])
	bR2 , _ := strconv.Atoi(strIntB[1])
	R1 := aR1 * bR1 - aR2 * bR2
	R2 := aR1 * bR2 + aR2 * bR1

	return fmt.Sprintf("%v+%vi", R1, R2)
}
```

###### tags: `LeetCode` `python` `golang` `Complex Number Multiplication` 