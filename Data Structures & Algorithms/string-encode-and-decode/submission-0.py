class Solution:

    def encode(self, strs: List[str]) -> str:
        ret_str = []
        for s in strs:
            e = str(len(s)) + "#"
            ret_str.append(e)
            ret_str.append(s)
        print(ret_str)
        return ''.join(ret_str)

    def decode(self, s: str) -> List[str]:
        """
        3#car4#were
        """
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res