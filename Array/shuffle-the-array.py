# https://leetcode.com/problems/shuffle-the-array/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for idx in range(0,n):
            ans.append(nums[idx])
            ans.append(nums[idx+n])
             
        
        return ans
               
                
                
