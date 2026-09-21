class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x[0])
        res = [intervals[0]]

        for interval in intervals[1:]:
            if res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(interval[1], res[-1][1])
        return res
