# link to problem : https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        stack  = []
        ans = []
        while True:
                if curr is not None:
                    stack.append(curr)
                    curr = curr.left
                elif(stack):
                    curr = stack.pop()
                    print(curr.val)
                    ans.append(curr.val)
                    curr = curr.right
                else:
                    break
        return ans
                    
       
 # -------------------------- Recursive Way ---------------------------------------------------------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
res = []
class Solution:
    def __inti__(self):
        global res
        res = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: 
                global res
                return res
        self.inorderTraversal(root.left)
        res.append(root.val)
        self.inorderTraversal(root.right)
        
        return res
        
