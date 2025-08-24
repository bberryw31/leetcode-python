class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_buy = 10 ** 4
        for price in prices:
            if price < min_buy:
                min_buy = price
            else:
                res = max(price - min_buy, res)
        return res