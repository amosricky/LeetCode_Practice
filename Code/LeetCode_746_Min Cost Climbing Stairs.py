class Solution:
    def minCostClimbingStairs(self, cost):
        minCost = []
        minCost.append(cost[0])
        minCost.append(cost[1])

        for i in range(2, len(cost)):
            value = min(minCost[i-1], minCost[i-2]) + cost[i]
            minCost.append(value)
        return min(minCost[-1], minCost[-2])


myClass = Solution()
result = myClass.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
print(result)

