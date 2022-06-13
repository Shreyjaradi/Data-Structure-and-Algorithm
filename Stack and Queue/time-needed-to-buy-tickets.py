# link to problem : https://leetcode.com/problems/time-needed-to-buy-tickets/
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n_sec = 0
        while(tickets[k] > 0):
            for i in range(0,len(tickets)):
                if tickets[i] > 0 and tickets[k] > 0:
                    tickets[i] = tickets[i] -1
                    n_sec = n_sec  + 1
        return n_sec
                    
                    
        
