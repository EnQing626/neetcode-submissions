"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # 1. 按照开始时间排序
        intervals.sort(key=lambda x: x.start)
        
        # 2. 检查是否有冲突
        for i in range(1, len(intervals)):
            # 如果前一个会议结束时间大于当前会议开始时间，说明冲突
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True