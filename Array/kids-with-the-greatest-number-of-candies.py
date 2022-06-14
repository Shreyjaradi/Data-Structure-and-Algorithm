# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [True] * len(candies)
        max_one = max(candies)
        for i in range(0, len(candies)):
            if(candies[i] + extraCandies < max_one):
                result[i] = False
        return result 
        
