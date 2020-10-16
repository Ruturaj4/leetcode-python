# armstrong number

class Solution:
    def isArmstrong(self, N: int) -> bool:
        return N == sum([int(n)**len(str(N)) for n in str(N)])

# another solution
class Solution:
    def isArmstrong(self, N: int) -> bool:
        k = math.floor(math.log10(N)) + 1
        tot =0
        C = N
        while C:
            tot += (C % 10) ** k
            C //= 10
        return tot == N
