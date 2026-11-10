"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        # 1. 先按照会议开始时间排序
        intervals.sort(key=lambda x: x.start)
        
        # 2. 最小堆，维护正在使用的会议室的结束时间
        heap = []
        
        for interval in intervals:
            start = interval.start
            end = interval.end
            
            # 3. 如果当前会议可以复用一个会议室（前面的会议已结束）
            if heap and heap[0] <= start:
                heapq.heappop(heap)
            
            # 4. 加入当前会议的结束时间
            heapq.heappush(heap, end)
        
        # 5. 最后的堆大小就是需要的会议室数量
        return len(heap)