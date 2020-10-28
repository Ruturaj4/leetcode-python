#Design a max stack that supports push, pop, top, peekMax and popMax.

# push(x) -- Push element x onto stack.
# pop() -- Remove the element on top of the stack and return it.
# top() -- Get the element on the top.
# peekMax() -- Retrieve the maximum element in the stack.
# popMax() -- Retrieve the maximum element in the stack, and remove it.
# If you find more than one maximum elements, only remove the top-most one.

# my first attempt
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxstack = []


    def push(self, x: int) -> None:
        self.maxstack.append(x)

    def pop(self) -> int:
        return self.maxstack.pop()

    def top(self) -> int:
        return self.maxstack[-1]

    def peekMax(self) -> int:
        return max(self.maxstack)

    def popMax(self) -> int:
        cur = 0
        maximum = -float('inf')
        for i,v in enumerate(self.maxstack):
            if v>=maximum:
                maximum = v
                cur =i
        return self.maxstack.pop(cur)

# with improved time
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxstack = []


    def push(self, x: int) -> None:
        self.maxstack.append(x)

    def pop(self) -> int:
        return self.maxstack.pop()

    def top(self) -> int:
        return self.maxstack[-1]

    def peekMax(self) -> int:
        return max(self.maxstack)

    def popMax(self) -> int:
        self.maxstack = self.maxstack[::-1]
        temp = self.maxstack.pop(self.maxstack.index(max(self.maxstack)))
        self.maxstack = self.maxstack[::-1]
        return temp

# another solution
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.maxstack = []


    def push(self, x: int) -> None:
        cur = self.peekMax()
        if cur == None or x>cur:
            cur = x
        self.maxstack.append((x,cur))

    def pop(self) -> int:
        return self.maxstack.pop()[0] if self.maxstack else None

    def top(self) -> int:
        return self.maxstack[-1][0] if self.maxstack else None

    def peekMax(self) -> int:
        return self.maxstack[-1][1] if self.maxstack else None

    def popMax(self) -> int:
        cur = self.maxstack[-1][1]
        temp =[]
        while self.maxstack[-1][0]!=cur:
            temp.append(self.pop())
        self.pop()
        for i in reversed(temp):self.push(i)
        return cur
