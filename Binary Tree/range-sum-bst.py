# https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
            self.result = 0 
            def dfs(node, low, high):
                if not node:
                    return 0
                if (node.val >= low and node.val <= high):
                    self.result += node.val
                left = dfs(node.left, low, high)
                right = dfs(node.right, low, high)
                
                return self.result
            return dfs(root, low, high)
