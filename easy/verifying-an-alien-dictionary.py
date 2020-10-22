class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {v:i for i,v in enumerate(order)}
        def compare(word1, word2):
            i,j, compare_var=0,0,0
            while i<len(word1) and j<len(word2) and compare_var==0:
                compare_var = dic[word1[i]]-dic[word2[i]]
                i += 1
                j += 1
            if compare_var==0:
                return len(word1) - len(word2)
            else:
                return compare_var

        for i in range(len(words)-1):
            if compare(words[i], words[i+1])>0:
                return False
        return True

# another solution
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {v:i for i,v in enumerate(order)}
        for i in range(len(words)-1):
            j,k,compare_var = 0,0,0
            while j<len(words[i]) and k<len(words[i+1]) and compare_var==0:
                compare_var = dic[words[i][j]] - dic[words[i+1][k]]
                j+=1
                k+=1
            if compare_var==0:
                compare_var = len(words[i])-len(words[i+1])
            if compare_var > 0:
                return False
        return True
# another solution
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # s = 'abcdefghijklmnopqrstuvwxyz'
        dic = {v:i for i,v in enumerate(order)}

        for i in range(len(words)-1):
            j,k =0,0
            while j<len(words[i]) and k<len(words[i+1]):
                if dic[words[i][j]] != dic[words[i+1][k]]:
                    if dic[words[i][j]] > dic[words[i+1][k]]:
                        return False
                    break
                j+=1
                k+=1
            else:
                if len(words[i]) > len(words[i+1]):
                    return False
        return True
