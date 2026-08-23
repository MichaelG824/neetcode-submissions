class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30, 38]
        # [(5, 40)]
        # [1, 4, 1, 2, 1, 0, 0]
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                res[stack[-1][0]] = i - stack[-1][0] 
                stack.pop()
            stack.append((i, temperatures[i]))
            
        return res

