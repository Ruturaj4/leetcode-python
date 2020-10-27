#Input: [7,1,5,3,6,4]
#Output: 5
#Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#Not 7-1 = 6, as selling price needs to be larger than buying price.
#Input: [7,6,4,3,1]
#Output: 0
#Explanation: In this case, no transaction is done, i.e. max profit = 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices:
            minimum, maximum, result = prices[0],0,[]
            for i in prices:
                if i< minimum:
                    minimum = i
                    maximum =0
                elif i>maximum:
                    maximum = i
                    result.append(maximum - minimum)
            return max(result)
        else: return 0

#another solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices:
            minimum, maximum, result = prices[0],0,0
            for i in prices:
                if i< minimum:
                    minimum = i
                    maximum =0
                elif i>maximum:
                    maximum = i
                    result = max(result, maximum-minimum)
            return result
        else: return 0

# another solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum, result = float('inf'),0
        for i in prices:
            minimum = min(minimum, i)
            temp = i - minimum
            result = max(result, temp)
        return result
