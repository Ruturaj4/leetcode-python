#There is a special keyboard with all keys in a single row.
#Given a string keyboard of length 26 indicating the layout
#of the keyboard (indexed from 0 to 25), initially your finger
#is at index 0. To type a character, you have to move your finger to the index
#of the desired character. The time taken to move your finger from index i
#to index j is |i - j|.

#You want to type a string word. Write a function to calculate how much
#time it takes to type it with one finger.

# naive solution
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        i = 0
        last = 0
        for l in word:
            last += abs(keyboard.index(l) - i)
            i = keyboard.index(l)
        return last

# this is a more verbous but improved solution using dictionary
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pointer = 0
        last=0
        keys = {}
        for i,l in enumerate(keyboard):
            keys[l]=i
        for l in word:
            last += abs(keys[l] - pointer)
            pointer = keys[l]
        return last

# even faster
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        pointer = 0
        last=0
        dic = {k:v for v,k in enumerate(keyboard)}
        for l in word:
            current = dic[l]
            last += abs(current - pointer)
            pointer = current
        return last
