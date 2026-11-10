class MedianFinder:

    def __init__(self):
        self.minheap=[]
        self.maxheap=[]
        self.count=0

    def addNum(self, num: int) -> None:
        self.count+=1
        heapq.heappush(self.maxheap,(-num,num))
        _,maxnum=heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap,maxnum)
        if len(self.maxheap)<len(self.minheap):
            minnum=heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap,(-minnum,minnum))

    def findMedian(self) -> float:
        if self.count%2==1:
            _,maxres=self.maxheap[0]
            return float(maxres)
        elif self.count%2==0:
            _,maxres=self.maxheap[0]
            minres=self.minheap[0]
            return (maxres+minres)/2