# Given a binary tree, return all root-to-leaf paths.
#
# Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(root, cur, result):
            if not root.left and not root.right:
                result.append(cur+str(root.val))
            if root.left:
                dfs(root.left, cur+str(root.val)+"->", result)
            if root.right:
                dfs(root.right, cur+str(root.val)+"->", result)
        if not root: return []
        result = []
        dfs(root, "", result)
        return result

# another way
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        result, stack = [], [(root, "")]
        while stack:
            node, cur = stack.pop()
            if not node.left and not node.right:
                result.append(cur+str(node.val))
            if node.right:
                stack.append((node.right, cur+str(node.val)+"->"))
            if node.left:
                stack.append((node.left, cur+str(node.val)+"->"))
        return result
