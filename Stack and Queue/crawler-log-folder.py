#Link to problem : https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for i in range(0, len(logs)):
            if(logs[i] == '../'):
                count = max(count-1,0)
            elif(logs[i] != './'):
                count = count + 1
        return count
                
        
