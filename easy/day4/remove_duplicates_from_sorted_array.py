class Solution:
    def removeDuplicates(self, nums: 'List[int]') -> 'int':
        stack = []
        n = 0
        while(n < len(nums)):
            if not stack:
                stack.append(nums[n])
            else:
                temp = stack.pop()
                if temp == nums[n]:
                    del(nums[n])
                    stack.append(temp)
                    continue
                else:
                    stack.append(nums[n])
            n+=1