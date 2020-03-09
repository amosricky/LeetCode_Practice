class Solution:
    def __init__(self):
        self.min_coins = float('inf')

    def coinChange(self, coins: "List[int]", amount: "int") -> "int":
        coins.sort(reverse=True)
        self.GreedCoinChange(coins, amount, 0, 0)
        return self.min_coins if self.min_coins < float("inf") else -1

    def GreedCoinChange(self, coins, remainder, point, coin_count):

        if remainder == 0 and coin_count < self.min_coins:
            self.min_coins = coin_count
            return

        if remainder <= 0 or coin_count >= self.min_coins or point >= len(coins):
            return

        if remainder < coins[point]:
            self.GreedCoinChange(coins, remainder, point + 1, coin_count)
            return

        maxAmountPossible = (self.min_coins - coin_count) * coins[point]
        if remainder < maxAmountPossible:
            tempCount = int(remainder / coins[point])
            for i in range(tempCount + 1, -1, -1):
                self.GreedCoinChange(coins, remainder - i * coins[point], point + 1, coin_count + i)


coins = [259, 78, 94, 130, 493, 4, 168, 149]
amount = 4769
myClass = Solution()
result = myClass.coinChange(coins, amount)
print(result)
