class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # AAABAB
        d = {}
        
        longest_repeating_char_len = 0
        l = 0
        max_f = 0
        for r in range(len(s)):
            d[s[r]] = 1 + d.get(s[r], 0)
            d_max = 0
            for val in d.values():
                d_max = max(d_max, val)
            max_f = max(max_f, d_max)
            while r - l + 1 - max_f > k:
                d[s[l]] -= 1 
                l += 1
            longest_repeating_char_len = max(r - l + 1, longest_repeating_char_len)
            
        return longest_repeating_char_len
