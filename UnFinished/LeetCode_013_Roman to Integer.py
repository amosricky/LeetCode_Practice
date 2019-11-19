class Solution:
    def romanToInt(self, s: str) -> int:

        single = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        double = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        target = s
        result = 0
        lastAdd = None

        while(len(target)!=0):
            if(target[0:2] in double.keys()):
                tempAdd = double[target[0:2]]
                target = target[2:]
            elif(target[0] in single.keys()):
                tempAdd = single[target[0]]
                target = target[1:]
            else:
                return "Error!"

            if((lastAdd!=None) and (lastAdd<tempAdd)):
                return "Error!"

            result += tempAdd
            lastAdd = tempAdd

        return result

myClass = Solution()
reverseResult = myClass.romanToInt("MCMXCIV")
print(reverseResult)