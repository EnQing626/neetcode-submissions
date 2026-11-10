class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_={}
        for i in range(len(nums)):
            map_[nums[i]]=map_.get(nums[i],0)+1
        pri_heap=[]
        for key, freq in map_.items():
            heapq.heappush(pri_heap,(freq,key))
            if len(pri_heap)>k:
                heapq.heappop(pri_heap)
        result=[0]*k
        for i in range(k-1,-1,-1):
            result[i]=heapq.heappop(pri_heap)[1]
        return result