# LeetCode Problem link : https://leetcode.com/problems/baseball-game/

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
