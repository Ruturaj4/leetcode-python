# Given a sorted array nums, remove the duplicates in-place such that each element
# appears only once and returns the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the
# input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 1
        for i in range(0, len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[index] = nums[i+1]
                index +=1
        return index

# another solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for i in range(1, len(nums)):
            if nums[index] != nums[i]:
                index +=1
                nums[index] = nums[i]
        return index+1
