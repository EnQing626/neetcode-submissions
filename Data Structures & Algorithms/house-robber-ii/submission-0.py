class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]

        def rob(nums: List[int]) -> int:
            if len(nums) == 0:
                return 0
            if len(nums) == 1:
                return nums[0]
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            return dp[-1]
        val1=rob(nums[1:])
        val2=rob(nums[:-1])
        return max(val1,val2)