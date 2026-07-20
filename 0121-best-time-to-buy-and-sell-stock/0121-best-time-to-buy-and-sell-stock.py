class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minm=prices[0]
        profit = 0

        for i in prices:
            if i<minm:
                minm=i

            curprofit = i - minm

            if curprofit > profit:
                profit=curprofit
        return profit
            


        



        