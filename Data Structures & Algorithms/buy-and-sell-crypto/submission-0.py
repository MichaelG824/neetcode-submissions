class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_val = 101
        res = 0
        for p in prices:
            if min_val > p:
                min_val = p
            else:
                res = max(res, p - min_val)
        return res