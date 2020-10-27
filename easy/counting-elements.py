#Given an integer array arr, count how many elements x there are, such that
#x + 1 is also in arr.

#If there're duplicates in arr, count them seperately.

# my initial attempt O(n**2)
class Solution:
    def countElements(self, arr: List[int]) -> int:
        result = 0
        for i in arr:
            if i+1 in arr:
                result += 1
        return result

# one liner O(n**2)
class Solution:
    def countElements(self, arr: List[int]) -> int:
        return sum(1 for i in arr if i+1 in arr)

# set improves the above solutions O(n)
class Solution:
    def countElements(self, arr: List[int]) -> int:
        temp = set(arr)
        result =0
        for i in arr:
            if i+1 in temp:
                result += 1
        return result

# another solution - O(n)logn
class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr = sorted(arr)
        result =0
        run_length = 1
        for i in range(len(arr)-1):
            if arr[i] != arr[i+1]:
                if arr[i]+1 == arr[i+1]:
                    result += run_length
                run_length = 0
            run_length +=1
        return result
