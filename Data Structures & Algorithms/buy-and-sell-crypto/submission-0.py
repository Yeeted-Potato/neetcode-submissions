class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0]
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit.append(prices[j] - prices[i])
        profit.sort()
        return profit.pop()