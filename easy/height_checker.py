# Students are asked to stand in non-decreasing order of heights for an
#annual photo.

#Return the minimum number of students that must move in order for all
# students to be standing in non-decreasing order of height.

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum([1 for i,j in enumerate(sorted(heights)) if heights[i]!=j])

# better version of the above solution
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        s =sorted(heights)
        return sum([heights[i]!=j for i,j in enumerate(s)])

# zipping lists
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(i!=j for i,j in zip(heights, sorted(heights)))
