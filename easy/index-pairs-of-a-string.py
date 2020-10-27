#Given a text string and words (a list of strings), return all index pairs
#[i, j] so that the substring text[i]...text[j] is in the list of words.

# using trie data structure
class Trie:
    def __init__(self):
        self.root = {"*":"*"}
    def add_word(self, word):
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]
        cur["*"] = "*"
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        trie = Trie()
        l = len(text)
        for word in words:
            trie.add_word(word)
        temp = []
        for i in range(l):
            node = trie.root
            j = i
            while node and j<l and text[j] in node:
                node = node[text[j]]
                if "*" in node: temp.append([i,j])
                j +=1
        return temp

# another solution
class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        temp = []
        l = len(text)
        for i in range(l):
            for w in words:
                j = i+len(w)-1
                if j<l and text[i:j+1]==w:
                    temp.append([i,j])
        return sorted(temp)
