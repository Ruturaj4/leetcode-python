#Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
#Output: [0,4,1,3,2]

#Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
#Output: [0,1,2,3,4]

#Input: nums = [1], index = [0]
#output: [1]

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        temp = []
        for i,j in zip(index, nums):
            temp[i:0] = [j]
        return temp

# another solution using clear syntax
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            if index[i] == len(nums):
                target.append(nums[i])
            else:
                target = target[:index[i]] + [nums[i]] + target[index[i]:]
        return target

# using insert
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target
