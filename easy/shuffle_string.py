#Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
#Output: "leetcode"

# one liner
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return "".join([i[0] for i in sorted(zip(s, indices), key=itemgetter(1))])

# faster and clearer solution
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        li = [0]*len(s)
        for i,v in enumerate(indices):
            li[v] = s[i]
        return "".join(li)
