#link to problem : https://leetcode.com/problems/make-the-string-great/

class Solution:
    def makeGood(self, s: str) -> str:
        stk = [s[0]]
        for c in s[1:]:
            if len(stk) > 0:
                if c.islower():
                    if ord(stk[-1]) + 32 == ord(c):
                        stk.pop()
                    else:
                        stk.append(c)
                    
                elif c.isupper():
                    if ord(stk[-1]) -32 == ord(c):
                        stk.pop()
                    else:
                        stk.append(c)
                    
            else:
                stk.append(c)
                
        return "".join(stk)
                
            
                
                    
                    
        
