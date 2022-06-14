# https://leetcode.com/problems/decompress-run-length-encoded-list/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        temp_list = []
        for idx in range(0,len(nums),1):
            print(idx)
            count = 0
            count = nums[idx - 1] 
            temp_list += count * [nums[idx]]
        return temp_list 
