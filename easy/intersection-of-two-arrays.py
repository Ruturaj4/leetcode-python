#Given two arrays, write a function to compute their intersection.

# my initial attempt:
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [n for n in set(nums1) if n in nums2]
# another attempt:
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set([n for n in nums1 if n in nums2])

# another approach
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)
