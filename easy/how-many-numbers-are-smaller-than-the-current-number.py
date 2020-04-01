# how-many-numbers-are-smaller-than-the-current-number

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        return [sorted_nums.index(n) for n in nums]
