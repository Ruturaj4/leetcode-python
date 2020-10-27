# Given numBottles full water bottles, you can exchange numExchange empty water
#bottles for one full water bottle.

#The operation of drinking a full water bottle turns it into an empty bottle.

#Return the maximum number of water bottles you can drink.

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles
        while numBottles>=numExchange:
            ans+=numBottles//numExchange
            numBottles = numBottles//numExchange+numBottles%numExchange
        return ans

# one liner
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        return numBottles + (numBottles -1)//(numExchange-1)
