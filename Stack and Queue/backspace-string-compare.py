#link to problem : https://leetcode.com/problems/backspace-string-compare/


class Solution:
    def cmp(self, s):
        stk = []
        for i in s:
            if i != '#':
                stk.append(i)
            else:
                if stk:
                    stk.pop()
        return stk
        
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.cmp(s) == self.cmp(t)
        
        
