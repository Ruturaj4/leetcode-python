# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# topdown approach
class Solution:
    result = 0
    def recursive(self, root, depth):
        if root:
            if not root.left and not root.right:
                self.result = max(self.result, depth)
            self.recursive(root.left, depth+1)
            self.recursive(root.right, depth+1)
    def maxDepth(self, root: TreeNode) -> int:
        self.recursive(root, 1)
        return self.result

# bottomup approach
class Solution:
    def recursive(self, root):
        if root:
            left = self.recursive(root.left)
            right = self.recursive(root.right)
            return max(left,right)+1
        else: return 0
    def maxDepth(self, root: TreeNode) -> int:
        return self.recursive(root)
