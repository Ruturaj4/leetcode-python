# Given a list of scores of different students, return the average score
#of each student's top five scores in the order of each student's id.
#Each entry items[i] has items[i][0] the student's id, and items[i][1] the
#student's score.  The average score is calculated using integer division.

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dic = {i:[] for i,j in items}
        for i,j in items:
            dic[i].append(j)
        return [[k,sum(sorted(v, reverse=True)[:5])//len(sorted(v, reverse=True)[:5])] for k,v in dic.items()]
