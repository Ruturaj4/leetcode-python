# Given two lists Aand B, and B is an anagram of A. B is an anagram of A means
#B is made by randomizing the order of the elements in A.
#We want to find an index mapping P, from A to B. A mapping P[i] = j means
#the ith element in A appears in B at index j.

# quick solution using dictionary
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        dic = {k:v for v,k in enumerate(B)}
        return [dic[x] for x in A]
