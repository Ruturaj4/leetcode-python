# Design a data structure that accepts a stream of integers and checks if
# it has a pair of integers that sum up to a particular value.
#
# Implement the TwoSum class:
#
# TwoSum() Initializes the TwoSum object, with an empty array initially.
# void add(int number) Adds number to the data structure.
# boolean find(int value) Returns true if there exists any pair of numbers
# whose sum is equal to value, otherwise, it returns false.

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = []


    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.arr.append(number)


    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        self.arr.sort()
        i,j = 0,len(self.arr)-1
        while i<j:
            cur = self.arr[i]+self.arr[j]
            if cur > value:
                j-=1
            elif cur < value:
                i+=1
            else:
                return True
        return False




# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)

# another solution
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = {}


    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.nums:
            self.nums[number]+=1
        else:
            self.nums[number] = 1


    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.nums:
            temp = value - num
            if num != temp:
                if temp in self.nums:
                    return True
            elif self.nums[num] > 1:
                return True
        return False
