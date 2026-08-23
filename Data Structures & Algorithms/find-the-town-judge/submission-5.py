class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outcoming = defaultdict(int)

        for i in range(len(trust)):
            incoming[trust[i][1]] += 1
            outcoming[trust[i][0]] += 1
        print(incoming)
        print(outcoming)
        for i in range(1, n + 1):
            if incoming[i] == n - 1 and outcoming[i] == 0:
                return i
        return -1