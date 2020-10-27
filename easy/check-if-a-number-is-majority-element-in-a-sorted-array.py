#Given an array nums sorted in non-decreasing order, and a number target,
#return True if and only if target is a majority element.

#A majority element is an element that appears more than N/2 times in an array of length N.

# my initial attempt
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        count = collections.Counter(nums)
        if target in count and count[target]>len(nums)/2:
            return True
        return False

# one liner
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        return nums.count(target) > len(nums)//2

#using bisect
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if nums[n//2]!=target:
            return False
        return bisect.bisect_right(nums, target)-bisect.bisect_left(nums, target)>n//2

# another solution, which uses a custom bisect function
class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        def bisect(i,j):
            l,h = 0,len(i)
            while l<h:
                mid = (l+h)//2
                if i[mid]<j:
                    l = mid +1
                else:
                    h = mid
            return l
        n = len(nums)
        if nums[n//2]!=target:
            return False
        return bisect(nums, target+1)-bisect(nums, target)>n//2
