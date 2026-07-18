class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i: i[0])
        merged = []
        cur = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= cur[1]:
                cur = [cur[0], max(cur[1], intervals[i][1])]
            else:
                merged.append(cur)
                cur = intervals[i]

        merged.append(cur)

        return merged