#Input: points = [[1,1],[3,4],[-1,0]]
#Output: 7
#Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] ->
#[2,3] -> [1,2] -> [0,1] -> [-1,0]
#Time from [1,1] to [3,4] = 3 seconds
#Time from [3,4] to [-1,0] = 4 seconds
#Total time = 7 seconds


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        temp = 0
        for i in range(0,len(points)-1):
            temp += max(abs(points[i][0]-points[i+1][0]), abs(points[i][1]-points[i+1][1]))
        return temp

# one liner
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return sum(max(abs(c-p) for c,p in zip(x,y)) for x,y in zip(points, points[1:]))
