#Given an array of meeting time intervals consisting of start and end
#times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals)
        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]:
                return False
        return True

#another solution
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        return not any(intervals[i][-1]>intervals[i+1][0] for i in range(len(intervals)-1))
