class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=-1
        temp=0
        for i in range(len(nums)):
            temp+=nums[i]
            if temp<0:
                temp=0
            elif temp>res:
                res=temp
        return res
                