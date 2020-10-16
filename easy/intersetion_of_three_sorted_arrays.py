# Given three integer arrays arr1, arr2 and arr3 sorted in strictly
# increasing order, return a sorted array of only the integers that
# appeared in all three arrays.

# simple solution
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        return sorted(set(arr1)&set(arr2)&set(arr3))

# using method
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        def intersection(a1, a2):
            i = j =0
            final = []
            while i<len(a1) and j<len(a2):
                if a1[i]<a2[j]:
                    i += 1
                elif a1[i]>a2[j]:
                    j +=1
                else:
                    final.append(a1[i])
                    i +=1
                    j +=1
            return final
        return intersection(intersection(arr1, arr2), arr3)
