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
