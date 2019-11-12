class Solution:
    def maxProfit(self, prices: 'List[int]') -> 'int':
        profit = 0
        max = 0

        for i in range(1, len(prices)):
            temp = prices[i] - prices[i - 1]
            if profit + temp > 0:
                profit += temp
            else:
                profit = 0
            if profit > max:
                max = profit

        return max


myClass = Solution()
result = myClass.maxProfit([1, 2, 11, 4, 7])
print(result)
