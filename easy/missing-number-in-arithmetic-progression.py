#In some array arr, the values were in arithmetic progression:
#the values arr[i+1] - arr[i] are all equal for every 0 <= i < arr.length - 1.

#Then, a value from arr was removed that was not the first or last value in the array.
#Return the removed value.

# my initial attempt:
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        if len(set(arr)) == 1:
            return arr[0]
        temp = float('inf')
        arr.sort()
        for i in range(len(arr)-1):
            temp = min(temp, arr[i+1]-arr[i])
        return [item for item in range(arr[0],arr[-1],temp) if item not in arr][0]

# another solution - this is very hard to find
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        return (min(arr)+max(arr))*(len(arr)+1)//2 -sum(arr)

# another easy to understand solution
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff = (arr[-1]-arr[0])//len(arr)
        if not diff:
            return arr[0]
        for i in range(1, len(arr)):
            if arr[i-1]+diff!=arr[i]:
                return arr[i-1]+diff
