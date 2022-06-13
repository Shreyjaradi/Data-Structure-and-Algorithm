Link to problem : https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return None
        p, q = 0, 0
        while(p!=len(nums1)):
            if(nums1[p] == nums2[q]):
                while(q!=len(nums2)-1):
                    if(nums1[p] < nums2[q]):
                        nums1[p] = nums2[q]
                        p = p +1
                        q = 0
                        break
                    else:
                        q = q +1
                if(q == len(nums2) -1 ):
                    if(nums1[p] < nums2[q] ):
                        nums1[p]= nums2[q]
                        p  = p +1 
                        q = 0
                    else:
                        nums1[p] = -1
                        p = p +1
                        q = 0
            else:
                q = q + 1
        
        return nums1
