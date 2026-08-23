class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        s1 = abc  [0,0, 0]
        s2 = lecabee
        """
        if len(s1) > len(s2):
            return False
        matches = 0

        # add to both array 
        arr1 = [0] * 26
        arr2 = [0] * 26

        for i in range(len(s1)):
            arr1[ord(s1[i]) - ord('a')] += 1
            arr2[ord(s2[i]) - ord('a')] += 1
        
        for i in range(26):
            matches += (1 if arr1[i] == arr2[i] else 0)
        j = 0
        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            r = ord(s2[i]) - ord('a')
            if arr2[r] == arr1[r]: matches -= 1
            arr2[r] += 1
            if arr2[r] == arr1[r]: matches += 1

            l = ord(s2[j]) - ord('a')
            if arr2[l] == arr1[l]: matches -= 1
            arr2[l] -= 1
            if arr2[l] == arr1[l]: matches += 1
            
            j += 1

        return matches == 26