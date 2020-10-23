#Given an array of integers nums.
#A pair (i,j) is called good if nums[i] == nums[j] and i < j.
#Return the number of good pairs.

# my initial attempt
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i, pairs = 0, 0
        while i<len(nums):
            j = i+1
            while j < len(nums):
                if nums[i] == nums[j]:
                    pairs += 1
                j +=1
            i+=1
        return pairs

# sorting the array first
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i, pairs = 0, 0
        while i<len(nums):
            j = i+1
            while j < len(nums):
                if nums[i] == nums[j]:
                    pairs += 1
                    j +=1
                else:
                    break
            i+=1
        return pairs

# another variation
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums = sorted(nums)
        i, pairs = 0, 0
        while i<len(nums):
            j = i+1
            while j<len(nums) and nums[i] == nums[j]:
                pairs += 1
                j +=1
            i+=1
        return pairs

# python one liner
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum(x*(x-1)//2 for x in collections.Counter(nums).values())
