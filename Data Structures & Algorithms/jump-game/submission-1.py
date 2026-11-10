class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #i is index of current num
        #cur_cover is the largest range of corrent num
        i=0
        cur_cover=0
        if len(nums) == 1:
            return True
        while i<=cur_cover:
            cur_cover=max(i+nums[i],cur_cover)
            if cur_cover>=len(nums)-1:
                return True
            i+=1
        return False