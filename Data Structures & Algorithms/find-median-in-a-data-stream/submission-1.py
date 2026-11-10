import heapq as hq
class MedianFinder:

    def __init__(self):
        self.small_heap = []
        self.max_heap = []
        self.count = 0

    def addNum(self, num: int) -> None:
        self.count += 1
        # 为什么要让num先进入大顶堆, 然后又进入小顶堆
        # 因为需要先顶出左边的最大的数字进入右边
        hq.heappush(self.max_heap, (-num, num))
        _, max_num = hq.heappop(self.max_heap)
        hq.heappush(self.small_heap, max_num)

        # 这个操作是为了让左边的大顶堆总是比右边的堆多一个数字
        if len(self.max_heap) < len(self.small_heap):
            min_num = hq.heappop(self.small_heap)
            hq.heappush(self.max_heap, (-min_num, min_num))

    def findMedian(self) -> float:
        if self.count % 2 == 1:
            _, max_num = self.max_heap[0]
            return float(max_num)
        else:
            _, left = self.max_heap[0]
            right = self.small_heap[0]
            return (left + right)/2
        
        