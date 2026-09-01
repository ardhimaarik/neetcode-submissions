class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        slow, fast = 0, 1
        while fast < len(prices): 
            
            if prices[fast] <= prices[slow]: 
                slow = fast
            else:
                maxprofit = max(maxprofit, prices[fast]-prices[slow])
            fast += 1 
        return maxprofit
        