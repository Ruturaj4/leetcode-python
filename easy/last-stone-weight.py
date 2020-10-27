#Input: [2,7,4,1,8,1]
#Output: 1

#We have a collection of stones, each stone has a positive integer weight.

#Each turn, we choose the two heaviest stones and smash them together.
#Suppose the stones have weights x and y with x <= y.  The result of this smash is:

#If x == y, both stones are totally destroyed;
#If x != y, the stone of weight x is totally destroyed, and the stone of weight
#y has new weight y-x.
#At the end, there is at most 1 stone left.  Return the weight of this stone
#(or 0 if there are no stones left.)

# my initial attempt
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            max1, max2 = stones[-1], stones[-2]
            if max1 == max2:
                stones = stones[:-2]
            else:
                stones = stones[:-2]
                stones.append(max1-max2)
            stones.sort()
        return stones[0] if stones else 0

# Another solution
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            max1=max(stones)
            stones.remove(max1)
            max2=max(stones)
            stones.remove(max2)
            if max1>max2:
                stones.append(max1-max2)
            elif max2>max1:
                stones.append(max2-max1)
        return stones[0] if stones else 0

# a solution using max heap - much better runtime
class Maxheap:
  def __init__(self, items):
    self.heap = [0]
    for i in items:
      self.heap.append(i)
      self.__floatup(len(self.heap) - 1)
  def push(self, data):
    self.heap.append(data)
    self.__floatup(len(self.heap)-1)
  def peek(self):
    if self.heap[1]:
      return self.heap[1]
    else:
      return False
  def pop(self):
    if len(self.heap) > 2:
      self.__swap(1, len(self.heap)-1)
      maximum = self.heap.pop()
      self.__floatdown(1)
    elif len(self.heap) == 2:
      maximum = self.heap.pop()
    else:
      maximum = False
    return maximum
  def __swap(self, i, j):
    self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
  def __floatup(self, index):
    parent = index//2
    if index <= 1:
      return
    if self.heap[index] > self.heap[parent]:
      self.__swap(index, parent)
      self.__floatup(parent)
  def __floatdown(self, index):
    left = index*2
    right = index*2+1
    largest = index
    if len(self.heap)> left and self.heap[largest] < self.heap[left]:
      largest = left
    if len(self.heap) > right  and self.heap[largest] < self.heap[right]:
      largest = right
    if largest != index:
      self.__swap(index, largest)
      self.__floatdown(largest)

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        m = Maxheap(stones)
        while len(m.heap) > 2:
            max1, max2= m.pop(), m.pop()
            if max1>max2:
                m.push(max1-max2)
            elif max2>max1:
                m.push(max2-max1)
        return m.heap[1] if len(m.heap)==2 else 0
