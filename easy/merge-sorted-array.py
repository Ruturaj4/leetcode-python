# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
#one sorted array.

# my initial attempt
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = n-1
        for i,v in reversed(list(enumerate(nums1))):
            if j<0: break
            if v == 0:
                nums1[i] = nums2[j]
            j -= 1
        nums1.sort()

# another solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m]+nums2)

# a clever solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1,p2,p = m-1,n-1,m+n-1
        while p1>=0 and p2>=0:
            if nums1[p1]<nums2[p2]:
                nums1[p]=nums2[p2]
                p2 -=1
            else:
                nums1[p] = nums1[p1]
                p1 -=1
            p-=1
        nums1[:p2+1]=nums2[:p2+1]

# a much better solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m-1,n-1
        p = m+n-1
        while p>=0:
            if p1<0:
                nums1[p] = nums2[p2]
                p2-=1
            elif p2<0:
                nums1[p] = nums1[p1]
                p1-=1
            else:
                if nums1[p1] < nums2[p2]:
                    nums1[p] = nums2[p2]
                    p2-=1
                else:
                    nums1[p] = nums1[p1]
                    p1-=1
            p-=1
