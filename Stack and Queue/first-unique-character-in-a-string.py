# Link to problem : https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1
        
        if len(s) == 1:
            return 0

        for i in s:   
            if(s.count(i) == 1):
                return s.index(i)
        return -1
