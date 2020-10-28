# Given a characters array tasks, representing the tasks a CPU needs to do,
# where each letter represents a different task. Tasks could be done in any order.
# Each task is done in one unit of time. For each unit of time, the CPU could
# complete either one task or just be idle.
#
# However, there is a non-negative integer n that represents the cooldown period
# between two same tasks (the same letter in the array), that is that there must be
# at least n units of time between any two same tasks.
#
# Return the least number of units of times that the CPU will take to finish all the given tasks.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cur, heap = 0,[]
        for k,v in collections.Counter(tasks).items():
            heapq.heappush(heap, (-1*v,k))
        while heap:
            i, temp = 0,[]
            while i<=n:
                cur +=1
                if heap:
                    x,y = heapq.heappop(heap)
                    if x!=-1:
                        temp.append((x+1,y))
                if not heap and not temp:
                    break
                else:
                    i+=1
            for item in temp:
                heapq.heappush(heap, item)
        return cur
