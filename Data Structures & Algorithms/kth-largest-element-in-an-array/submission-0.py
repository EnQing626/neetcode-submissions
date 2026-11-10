class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for x in nums:
            heapq.heappush(maxHeap, -x)
        for _ in range(k - 1):
            heapq.heappop(maxHeap)
        return -maxHeap[0]