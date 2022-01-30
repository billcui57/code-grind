def maxProfit(self, prices: List[int]) -> int:

    curMaxProfit = 0
    lowIndex = 0
    highIndex = 0

    while highIndex < len(prices) and lowIndex < len(prices):
        highPrice = prices[highIndex]
        lowPrice = prices[lowIndex]

        if lowPrice < highPrice:
            if highPrice - lowPrice > curMaxProfit:
                curMaxProfit = highPrice - lowPrice
            highIndex += 1
        else:
            lowIndex = highIndex
            highIndex += 1

    return curMaxProfit
