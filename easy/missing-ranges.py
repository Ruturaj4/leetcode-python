#You are given an inclusive range [lower, upper] and a sorted unique integer
#array nums, where all elements are in the inclusive range.

#A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

#Return the smallest sorted list of ranges that cover every missing number exactly.
#That is, no element of nums is in any of the ranges, and each missing number is in one of the ranges.

#Each range [a,b] in the list should be output as:

#"a->b" if a != b
#"a" if a == b

class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        temp = []
        for i in nums:
            if i > lower:
                if i-lower == 1:
                    temp.append(str(lower))
                else:
                    temp.append(str(lower)+"->"+str(i-1))
            lower = i+1
        if upper>lower:
            temp.append(str(lower)+"->"+str(upper))
        elif upper == lower:
            temp.append(str(lower))
        return temp

# another way
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        temp = []
        nums.append(upper+1)
        for i in nums:
            if i > lower:
                if i-lower == 1:
                    temp.append(str(lower))
                else:
                    temp.append(str(lower)+"->"+str(i-1))
            lower = i+1
        return temp
