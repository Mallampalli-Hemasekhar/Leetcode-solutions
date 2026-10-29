class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        i = 0
        while i < len(intervals):
            j = i + 1
            while j < len(intervals):
                if (intervals[i][0] <= intervals[j][1]
                    and intervals[j][0] <= intervals[i][1]):
                    intervals[i][0] = min(
                        intervals[i][0], intervals[j][0]
                    )
                    intervals[i][1] = max(
                        intervals[i][1], intervals[j][1]
                    )
                    intervals.pop(j)
                    j = i + 1
                else:
                    j += 1
            i += 1
        return intervals