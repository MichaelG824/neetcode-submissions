class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(curr_count):
            if curr_count in cache:
                return cache[curr_count]
            if curr_count == 0:
                return 0
            res = 1e9
            for coin in coins:
                if curr_count - coin >= 0:
                    res = min(res, 1 + dfs(curr_count - coin))
            cache[curr_count] = res
            return res

        min_coins = dfs(amount)
        return -1 if min_coins >= 1e9 else min_coins