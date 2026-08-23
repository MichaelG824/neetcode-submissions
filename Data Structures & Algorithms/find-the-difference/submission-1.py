class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        c_set = {}
        t_set = {}
        for c in s:
            if c in c_set:
                c_set[c] += 1
            else:
                c_set[c] = 1
        
        for c in t:
            if c in t_set:
                t_set[c] += 1
            else:
                t_set[c] = 1
        
        for c in t:
            if c not in c_set or c_set[c] != t_set[c]:
                return c
