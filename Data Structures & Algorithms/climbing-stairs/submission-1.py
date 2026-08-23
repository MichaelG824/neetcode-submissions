class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def climb(num):
            if num in cache:
                return cache[num]
            elif num < 0:
                return 0
            elif num == 0:
                return 1
            cache[num] = climb(num - 1) + climb(num - 2)
            return cache[num]
        return climb(n)