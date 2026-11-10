class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import collections
        que=collections.deque()
        res=[]
        for i in range(len(nums)):
            while que and nums[que[-1]]<nums[i]:
                que.pop()
            que.append(i)
            if que[0]<=i-k:
                que.popleft()
            if i>=k-1:
                res.append(nums[que[0]])
        return res