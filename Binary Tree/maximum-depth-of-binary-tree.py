------ link : https://leetcode.com/problems/maximum-depth-of-binary-tree/ -----------



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 
        else:
            left_leaf = self.maxDepth(root.left)
            right_leaf = self.maxDepth(root.right)
            return 1 + max(left_leaf, right_leaf)
