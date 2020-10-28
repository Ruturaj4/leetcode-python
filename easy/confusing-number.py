# Given a number N, return true if and only if it is a confusing number, which
# satisfies the following condition:
#
# We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are
# rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7
# are rotated 180 degrees, they become invalid.
# A confusing number is a number that when rotated 180 degrees becomes a
# different number with each digit valid.

class Solution:
    def confusingNumber(self, N: int) -> bool:
        temp = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        number = []
        for i in str(N)[::-1]:
            if i not in temp:
                return False
            number.append(temp[i])
        if "".join(number)!=str(N):
            return True

# another approach
class Solution:
    def confusingNumber(self, N: int) -> bool:
        temp = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        n = str(N)
        for i in n[::-1]:
            if i not in temp:
                return False
        for i in range((len(n)+1)//2):
            if temp[n[i]]!=n[-i-1]:
                return True
        return False
