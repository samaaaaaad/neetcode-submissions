class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_cp = prices[0]
        profit = 0
        for i in range(len(prices)):
            if min_cp > prices[i]:
                min_cp = prices[i]
            elif prices[i] - min_cp > profit:
                    profit = prices[i] - min_cp
        return profit