# Given a non-empty binary search tree and a target value,
# find the value in the BST that is closest to the target.
#
# Note:
#
# Given target value is a floating point.
# You are guaranteed to have only one unique value in the BST that is closest to the target.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        cur = root
        val = cur.val
        while cur:
            if abs(cur.val-target) <abs(val-target):
                val = cur.val
            if target<cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return val

# improving by not using cur
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        val = root.val
        while root:
            if abs(root.val-target) <abs(val-target):
                val = root.val
            if target<root.val:
                root = root.left
            else:
                root = root.right
        return val
