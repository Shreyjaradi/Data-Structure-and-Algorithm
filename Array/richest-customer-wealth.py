# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxamt = []
        total = 0
        for i in accounts :
            total = 0
            for j in i :
                total = total + j
            maxamt.append(total)
        max = 0
        for i in maxamt:
            if(max <=i):
                max = i
        
        return max
        
