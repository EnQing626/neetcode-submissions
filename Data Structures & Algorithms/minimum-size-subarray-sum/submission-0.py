class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums is None or len(nums)==0:
            return 0
        l,r=0,0
        res=len(nums)+1
        total=0
        while r<len(nums):
            total=total+nums[r]
            r+=1
            while total>=target:
                res=min(res,r-l)
                total=total-nums[l]
                l+=1
        if res==len(nums)+1:
            return 0
        else:
            return res