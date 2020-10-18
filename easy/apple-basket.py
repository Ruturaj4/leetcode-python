# You have some apples, where arr[i] is the weight of the i-th apple.
#You also have a basket that can carry up to 5000 units of weight.

#Return the maximum number of apples you can put in the basket.

# greedy solution
# try to add as many apples with lower weights as possible
class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        temp,j = 0,0
        for i,v in enumerate(sorted(arr)):
            temp+=v
            if temp > 5000:
                break
            j+=1
        return j

# another solution
class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        temp,j = 0,0
        arr = sorted(arr)
        while j<len(arr):
            temp+=arr[j]
            if temp > 5000:
                return j
            j+=1
        return j
