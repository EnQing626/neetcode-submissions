class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sumnum=sum(nums)
        if abs(target)>sumnum or (sumnum+target)%2==1:
            return 0
        bagsize=(sumnum+target)//2
        dp=[0]*(bagsize+1)
        dp[0]=1
        for i in range(len(nums)):
            for j in range(bagsize,nums[i]-1,-1):
                dp[j]+=dp[j-nums[i]]
        return dp[-1]