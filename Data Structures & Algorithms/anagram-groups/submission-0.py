class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        act
        """
        # get array of each and put in dictionary
        # [1,1,] -> ["a", b]
        d = {}
        ans = []
        for w in strs:
            v = [0 for _ in range(26)]
            for char in w:
                v[ord(char) - ord('a')] += 1
            if tuple(v) in d:
                d[tuple(v)].append(w)
            else:
                d[tuple(v)] = [w]


        for v in d.values():
            ans.append(v)
        return ans 