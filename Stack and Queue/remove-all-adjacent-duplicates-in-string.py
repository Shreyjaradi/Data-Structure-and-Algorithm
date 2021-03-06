# Leet Code Problem link : https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, s: str) -> str:
            stk = []
            stk.append("")
            for i in s:
                if (stk[-1] !=i):
                    stk.append(i)
                else:
                    stk.pop()
            return ''.join(stk[1:])
