class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        {
            X: 2
            Y: 2
        }
        """
        d = {}
        i = 0
        j = 0
        res = 0
        while j < len(s):
            if s[j] in d:
                d[s[j]] += 1
            else:
                d[s[j]] = 1
            max_val = 0
            for v in d.values():
                max_val = max(max_val, v)
            if j - i + 1 - max_val > k:
                d[s[i]] -= 1
                i += 1
            res = max(res, j - i + 1)
            j += 1
        return res