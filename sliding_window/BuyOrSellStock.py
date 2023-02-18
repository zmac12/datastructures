from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i = 0
        j = 1
        if len(prices) == 0:
            return 0
        while i < j and j < len(prices):
            PorL = prices[j] - prices[i]
            if PorL > profit:
                profit = PorL
            if prices[j] >= prices[i]:
                j += 1
                continue
            if prices[j] < prices[i]:
                j += 1
                i = j - 1
        return profit