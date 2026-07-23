class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        profit=0
        window=[]
        for right in range(len(prices)):
            ch= prices[right]
            window.append(ch)
            while prices[right]<prices[left]:
                window.remove(prices[left])
                left+=1
            profit=max(profit,prices[right]-prices[left])
        return profit 

        