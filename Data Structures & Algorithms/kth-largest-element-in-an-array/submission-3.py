class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for x in nums:
            heapq.heappush(maxHeap, -x)
        #print(maxHeap)
        # for i in range(k-1):
        #     heapq.heappop(maxHeap)
        while k-1>0:
            heapq.heappop(maxHeap)
            k-=1
        return -maxHeap[0]