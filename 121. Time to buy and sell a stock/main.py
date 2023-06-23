class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """


        lowest_point = prices[0]

        best_sell = 0

        for price in prices:
            if price < lowest_point:
                lowest_point = price
            sell_value = price - lowest_point
            if sell_value > best_sell:
                best_sell = sell_value

        return best_sell

