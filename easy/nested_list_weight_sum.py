# Given a nested list of integers, return the sum of all integers in the
#list weighted by their depth.
# Each element is either an integer, or a list -- whose elements may also be
#integers or other lists.

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        count =0
        depth =1
        def nested(li, count, depth):
            for i in li:
                if not i.isInteger():
                    count = nested(i.getList(), count, depth+1)
                else:
                    count += i.getInteger()*depth
            return count
        return nested(nestedList, count, depth)
