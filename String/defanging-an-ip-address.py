# link to problem : https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return str.replace(address, '.', '[.]')
        
