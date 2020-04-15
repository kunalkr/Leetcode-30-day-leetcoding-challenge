class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Let's be greedy
        N = len(prices)
        profit = bprice = 0
        last = float('inf')
        
        for i, price in enumerate(prices):
            next = prices[i+1] if i < N-1 else float('-inf')
            if price <= last and price < next:
                # buy
                bprice = price
            elif price > last and price >= next:
                # sell
                profit += (price - bprice)
            last = price
        return profit
