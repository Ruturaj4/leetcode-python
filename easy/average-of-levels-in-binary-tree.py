# Given a non-empty binary tree, return the average value of the nodes on each
# level in the form of an array.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        stack = []
        def average(node, depth):
            if node:
                if len(stack) <=depth:
                    stack.append([0,0])
                stack[depth][0]+=node.val
                stack[depth][1]+=1
                average(node.left, depth+1)
                average(node.right, depth+1)
        average(root,0)
        return [s/c for s,c in stack]

# another approach
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return []
        stack = [root]
        result = []
        while stack:
            total, count = 0, len(stack)
            for i in range(count):
                node = stack.pop(0)
                total += node.val
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            result.append(total/count)
        return result
