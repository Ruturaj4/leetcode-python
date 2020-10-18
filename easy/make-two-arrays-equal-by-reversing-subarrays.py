#Input: target = [1,2,3,4], arr = [2,4,1,3]
#Output: true

#Input: target = [3,7,9], arr = [3,7,11]
#Output: false

# I quickly figured out that by sorting and checking if two lists are equal
# might be the way

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
