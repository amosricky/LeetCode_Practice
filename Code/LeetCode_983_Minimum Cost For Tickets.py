class Solution:
    def mincostTickets(self, days: "List[int]", costs: "List[int]") -> "int":

        dayCost = [0] * (days[-1] + 1)
        for day in range(1, days[-1] + 1):
            if day not in days:
                dayCost[day] = dayCost[day - 1]
            else:
                dayCost[day] = min(dayCost[max(0, day - 1)] + costs[0], dayCost[max(0, day - 7)] + costs[1], dayCost[max(0, day - 30)] + costs[2])
        return dayCost[-1]


myClass = Solution()
result = myClass.mincostTickets([1,4,6,7,8,20], [2,7,15])
print(result)