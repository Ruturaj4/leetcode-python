class Solution(object):
    def twoSum(self, nums, target):
        for n in range(len(nums)-1):
            for i in range(len(nums)):
                if n == i:
                    continue
                if nums[n] + nums[i] == target:
                    return [n, i]