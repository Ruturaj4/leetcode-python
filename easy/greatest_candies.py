# Given the array candies and the integer extraCandies,
# where candies[i] represents the number of candies that the ith kid has.

# For each kid check if there is a way to distribute extraCandies
# among the kids such that he or she can have the greatest number of candies
# among them. Notice that multiple kids can have the greatest number of candie

# using list comprehension
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        return [True if (x+extraCandies)>=greatest else False for x in candies]

# using lambda
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        return map(lambda x: (x+extraCandies)>=greatest, candies)

# another simpler list comprehension
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        return [x+extraCandies>=greatest for x in candies]
