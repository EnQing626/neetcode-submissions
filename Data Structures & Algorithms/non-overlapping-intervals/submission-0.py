class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])  # 按左端点排序
        remove = 0
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            # 如果有重叠
            if intervals[i][0] < prev_end:
                remove += 1
                # 保留右端点更小的区间
                #Among the overlapping intervals, keep the one with smaller end time (minimizes chance of future overlap).
                prev_end = min(prev_end, intervals[i][1])
            else:
                prev_end = intervals[i][1]
        return remove