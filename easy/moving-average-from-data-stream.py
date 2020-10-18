# Given a stream of integers and a window size, calculate the moving
# average of all integers in the sliding window.

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.li = []

    def next(self, val: int) -> float:
        if len(self.li) <self.size:
            self.li.append(val)
            return sum(self.li)/len(self.li)
        else:
            self.li.pop(0)
            self.li.append(val)
            return sum(self.li)/len(self.li)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# another solution

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.li = []

    def next(self, val: int) -> float:
        if len(self.li) <self.size:
            self.li.append(val)
            return sum(self.li)/len(self.li)
        else:
            self.li.append(val)
            return sum(self.li[-self.size:])/len(self.li[-self.size:])

# fastser
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.li = []
        self.sum = 0

    def next(self, val: int) -> float:
        if len(self.li) == self.size:
            self.sum -= self.li.pop(0)
        self.sum += val
        self.li.append(val)
        return self.sum/len(self.li)
