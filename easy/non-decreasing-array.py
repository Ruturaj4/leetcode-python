#Given an array nums with n integers, your task is to check if it could
#become non-decreasing by modifying at most 1 element

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                count +=1
                if count>1:
                    return False
                if (nums[i-1] > nums[i+1]) and i!=0:
                    nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]
        return True

# another solution
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                count+=1
                if i<2 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return count<=1
