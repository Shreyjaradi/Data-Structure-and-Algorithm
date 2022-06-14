# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i=0
        ans = [0] * n
        while (i<n):
            if(i==0):
                ans[i] = nums[i]
            else:
                j=i
                while(j!=-1):
                    ans[i]= ans[i] + nums[j]
                    j = j -1
            i=i+1    
        return ans
