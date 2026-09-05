class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 0
        res = []
        while i < len(intervals):
            cur = intervals[i]
            i += 1
            while i < len(intervals) and intervals[i][0] <= cur[1]:
                cur[1] = max(cur[1], intervals[i][1])
                i += 1
            res.append(cur)

        return res