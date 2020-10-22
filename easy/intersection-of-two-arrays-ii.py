#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2,2]
#Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
#Output: [4,9]
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        i, j = 0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j+=1
            elif nums1[i] < nums2[j]:
                i +=1
            else:
                temp.append(nums1[i])
                i+=1
                j+=1
        return temp

# another solution using dictionary
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = []
        nums1 = collections.Counter(nums1)

        for x in nums2:
            if nums1[x] > 0:
                temp.append(x)
                nums1[x] -=1
        return temp

# take the hashmap of the smaller list, making it faster
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = []
        if nums1 > nums2:
            nums1, nums2 = nums2, nums1
        nums1 = collections.Counter(nums1)
        for x in nums2:
            if nums1[x] > 0:
                temp.append(x)
                nums1[x] -=1
        return temp
