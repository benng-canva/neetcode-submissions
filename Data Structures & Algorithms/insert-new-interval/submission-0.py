class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # insert to list
        l, r = 0, len(intervals)
        while l < r:
            m = (l + r) // 2

            interval = intervals[m]

            if interval[0] > newInterval[0]:
                r = m
            else:
                l = m + 1

        intervals = intervals[:l] + [newInterval] + intervals[l:]

        # merge
        merged = []
        curInterval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= curInterval[1]:
                curInterval = [curInterval[0], max(curInterval[1], intervals[i][1])]
            else:
                merged.append(curInterval)
                curInterval = intervals[i]

        merged.append(curInterval)
        
        return merged