# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:return []
        intervals.sort(key = lambda x:x.start)
        res = []
        i, start, end = 0, intervals[0].start, intervals[0].end
        for interval in intervals[1:]:
            if end < interval.start:
                res.append(Interval(start, end))
                start = interval.start
                end = interval.end
            elif end <= interval.end:
                end = interval.end
        res.append(Interval(start,end))
        return res

#better
def merge(self, intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i,
    return out