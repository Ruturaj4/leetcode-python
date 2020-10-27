#Given two strings A and B of lowercase letters, return true if you can swap two
#letters in A so the result is equal to B, otherwise, return false.

#Swapping letters is defined as taking two indices i and j (0-indexed) such that
#i != j and swapping the characters at A[i] and A[j]. For example, swapping at
#indices 0 and 2 in "abcd" results in "cbad"

# my initial attempt
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) == len(B):
            if A == "": return
            if A == B:
                count = collections.Counter(A)
                return max(count.values())>1
            else:
                result1 = []
                result2 = []
                for i in range(len(A)):
                    if A[i] != B[i]:
                        result1.append(A[i])
                        result2.append(B[i])
                return len(result1)==2 and set(result1)==set(result2)
        else:
            return False

# another attempt:
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) == len(B):
            if A == "": return
            if A == B:
                count = collections.Counter(A)
                return max(count.values())>1
            else:
                if collections.Counter(A) != collections.Counter(B):
                    return False
                result = 0
                for i in range(len(A)):
                    if A[i] != B[i]:
                        result +=1
                return result==2
        else:
            return False

# another attempt:
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) == len(B):
            if A == B:
                if A=="":
                    return False
                count = collections.Counter(A)
                return max(count.values())>1
            else:
                result = []
                for i in range(len(A)):
                    if A[i] != B[i]:
                        result.append(i)
                if len(result) == 2:
                    if A[result[0]] == B[result[1]] and A[result[1]] == B[result[0]]:
                        return True
                    else:
                        return False
                else: return False
        else:
            return False

# another solution with much better runtime
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B): return False
        if A == B:
            seen = set()
            for a in A:
                if a in seen:
                    return True
                seen.add(a)
            return False
        else:
            result = []
            for i in range(len(A)):
                if A[i] != B[i]:
                    result.append(i)
            if len(result) == 2:
                if A[result[0]] == B[result[1]] and A[result[1]] == B[result[0]]:
                    return True
                else:
                    return False
            else: return False
