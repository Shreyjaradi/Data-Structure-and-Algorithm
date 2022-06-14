#Link to problem : https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m = 0
        for i in sentences :
            m = max(m,i.count(" ")+1)
                
        return m
