#Given an array of integers arr, and three integers a, b and c.
#You need to find the number of good triplets.

#A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

#0 <= i < j < k < arr.length
#|arr[i] - arr[j]| <= a
#|arr[j] - arr[k]| <= b
#|arr[i] - arr[k]| <= c
#Where |x| denotes the absolute value of x.

#Return the number of good triplets.

# my initial attempt
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        i, count = 0,0
        while i<len(arr)-2:
            j = i+1
            while j < len(arr)-1:
                k = j+1
                while k < len(arr):
                    if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                        count +=1
                    k +=1
                j+=1
            i +=1
        return count

# improved solution
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        l = len(arr)
        count = 0
        for i in range(l-2):
            for j in range(i+1, l-1):
                for k in range(j+1,l):
                    if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                        count +=1
        return count

# with optimization
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        l = len(arr)
        count = 0
        for i in range(l-2):
            for j in range(i+1, l-1):
                if abs(arr[i]-arr[j])<=a:
                    for k in range(j+1,l):
                        if abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                            count +=1
        return count
