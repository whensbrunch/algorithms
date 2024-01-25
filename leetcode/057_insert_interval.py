class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        def overlaps(interval1, interval2):
            return (interval1[0] <= interval2[0] and interval1[1] >= interval2[0]) or (interval2[0] <= interval1[0] and interval2[1] >= interval1[0])

        def merge(interval1, interval2):
            return [min(interval1[0], interval2[0]), max(interval1[1], interval2[1])]

        res = []
        for interval in intervals:
            if overlaps(interval, newInterval):
                newInterval = merge(interval, newInterval)
            else:
                res.append(interval)
        
        res.append(newInterval)
        return sorted(res, key=lambda x: x[0])