# link to problem : https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

class Solution:
    def maxDepth(self, s: str) -> int:
        res = cur = 0
        for i in s:
            if i == '(':
                cur = cur + 1
                res = max(res, cur)
            elif i == ')':
                cur = cur - 1
        return res
                
        
