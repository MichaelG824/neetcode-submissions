class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tot = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                tot += (prices[i] - prices[i - 1])
        return tot
