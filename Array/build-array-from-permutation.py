
# Link to problem : https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        d = len(nums)
        ans = list()
        for i, val in enumerate(nums):
            ans.insert(i,nums[nums[i]])
        print(ans)
        
        return ans;
