class Solution:
    def validPalindrome(self, s: str) -> bool:
        def p(new_s, i, j):
            while i <= j:
                if new_s[i] != new_s[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        for i in range(len(s) // 2):
            if s[i] != s[len(s) - i - 1]:
                return p(s, i + 1, len(s) - i - 1) or p(s, i, len(s) - i - 2)   
        return True