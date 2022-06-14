# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
            p =0
            q = 1
            while(q <len(prices)):
                if(prices[q] <= prices[p]):
                        prices[p] = prices[p] - prices[q]
                        p = p + 1
                        q = p + 1
                else:
                    if (q == len(prices)-1 and prices[q]>prices[p]):
                        prices[p] = prices[p]
                        p = p +1
                        q = p+1
                    else:
                        q = q +1            
            return prices       
