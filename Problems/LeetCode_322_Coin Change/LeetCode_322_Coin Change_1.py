class Solution:
    def coinChange(self, coins: "List[int]", amount: "int") -> "int":
        coins.sort()
        count = [float("inf")] * (amount + 1)
        count[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                count[i] = min(count[i], count[i-coin] + 1)
        return count[-1] if count[-1] != float("inf") else -1

coins = [259, 78, 94, 130, 493, 4, 168, 149]
amount = 4769
myClass = Solution()
result = myClass.coinChange(coins, amount)
print(result)
