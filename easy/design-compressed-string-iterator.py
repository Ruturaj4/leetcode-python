# Design and implement a data structure for a compressed string iterator.
# The given compressed string will be in the form of each letter followed by
# a positive integer representing the number of this letter existing in the
# original uncompressed string.
#
# Implement the StringIterator class:
#
# next() Returns the next character if the original string still has uncompressed
# characters, otherwise returns a white space.
# hasNext() Returns true if there is any letter needs to be uncompressed in
# the original string, otherwise returns false.

class StringIterator:

    def __init__(self, compressedString: str):
        self.compressed = list(compressedString)[::-1]
        self.count = 0
        self.cur = ""

    def next(self) -> str:
        if not self.hasNext(): return " "
        if self.count==0:
            self.cur = self.compressed.pop()
            temp = 0
            while self.compressed and self.compressed[-1].isdigit():
                temp =temp*10+int(self.compressed.pop())
            self.count = temp
        self.count -=1
        return self.cur

    def hasNext(self) -> bool:
        return len(self.compressed)>0 or self.count>0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
