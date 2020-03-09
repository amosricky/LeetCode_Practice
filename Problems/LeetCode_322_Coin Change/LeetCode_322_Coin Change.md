# 【LeetCode】 322. Coin Change

## Description
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Note:
+ You may assume that you have an infinite number of each kind of coin.
## Example1:
```
Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
```
## Example 2:
```
Input: coins = [2], amount = 3
Output: -1
```

## Solution1
![](https://imgur.com/9b59plP.png)
* 參考上圖作法, 以 DFS 的方式做 DP 搜尋。

### Code1
```python
class Solution:
    def coinChange(self, coins: "List[int]", amount: "int") -> "int":
        coins.sort()
        count = [float("inf")] * (amount + 1)
        count[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                count[i] = min(count[i], count[i-coin] + 1)
        return count[-1] if count[-1] != float("inf") else -1
```
## Solution2
![](https://imgur.com/TLCxlBI.png)
* 參考上圖作法, 以 Greedy + DFS 做 DP 搜尋。
* 以最大 coin 開始帶入, 在依序帶入較小 coin, 過程中若超過 min_count 即可 break。

### Code2
```python
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
```
[Reference](https://www.youtube.com/watch?v=uUETHdijzkA)
###### tags: `LeetCode` `python` `Coin Change` 