class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        purchased = False
        min_buy, max_sell = None, None
        for i in range(len(prices) - 1):
            if not purchased and prices[i] < prices[i + 1]:
                min_buy = prices[i]
                purchased = True
            if purchased and prices[i] > prices[i + 1]:
                max_sell = prices[i]
                purchased = False
            if min_buy != None and max_sell != None:
                profit += (max_sell - min_buy)
                max_sell, min_buy = None, None
        if min_buy != None:
            profit += prices[-1] - min_buy
        return profit
        
            