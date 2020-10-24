#Given a list of words and two words word1 and word2, return the shortest
#distance between these two words in the list.

# initial attempt
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        dic = {}
        for i,w in enumerate(words):
            if w in dic:
                dic[w].append(i)
            else:
                dic[w] = [i]
        i,j=0,0
        pos1,pos2 = dic[word1], dic[word2]
        result = len(words)-1
        while i<len(pos1) and j<len(pos2):
            if pos1[i]<pos2[j]:
                result = min(result, pos2[j]-pos1[i])
                i+=1
            elif pos1[i]>pos2[j]:
                result = min(result, pos1[i]-pos2[j])
                j+=1
            else: return 0
        return result

# best solution
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        result = len(words)-1
        cur, index = None, 0
        for i, w in enumerate(words):
            if w not in (word1, word2): continue
            if cur and w!= cur:
                result = min(result, i-index)
            cur,index = w,i
        return result

# another solution
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        result = float('inf')
        p1, p2 = result, result
        for i, w in enumerate(words):
            if w == word1:
                p1 = i
            if w == word2:
                p2 = i
            result = min(result, abs(p1-p2))
        return result
