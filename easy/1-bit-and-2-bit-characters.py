class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        li = []
        for b in bits:
            if len(li) == 2:
                li =[]
            if b == 1:
                li.append(b)
            if b==0:
                if len(li) == 1:
                    li.append(b)
                else:
                    li = []
        if len(li) == 0:
            return True
        else:
            return False
