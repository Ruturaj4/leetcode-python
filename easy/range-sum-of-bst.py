# Given the root node of a binary search tree, return the sum of values of
# all nodes with value between L and R (inclusive).
#
# The binary search tree is guaranteed to have unique values.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# iterative solution
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        range_sum = 0
        stack = [root]
        while stack:
            cur = stack.pop()
            if cur:
                if cur.val in range(L,R+1):
                    range_sum+=cur.val
                if cur.val > L:
                    stack.append(cur.left)
                if cur.val < R:
                    stack.append(cur.right)
        return range_sum

# recursive solution
class Solution:
    range_sum = 0
    def recursive(self, node, l, r):
        if node:
            if node.val in range(l,r+1):
                self.range_sum += node.val
            if node.val > l:
                self.recursive(node.left, l, r)
            if node.val < r:
                self.recursive(node.right, l,r)
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.recursive(root,L,R)
        return self.range_sum
