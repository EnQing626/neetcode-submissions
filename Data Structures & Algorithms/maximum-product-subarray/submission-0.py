class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        res = nums[0]  # 结果变量初始化
        # dp[i][0]存储到当前层可达到最大
        # dp[i][1]存储到当前层可达到最小
        dp = [[0] * 2 for _ in range(len(nums))]
        dp[0][0], dp[0][1] = nums[0], nums[0]
        for i in range(1, len(nums)):
            left = nums[i] * dp[i - 1][0]
            right = nums[i] * dp[i - 1][1]
            # 因为当前nums[i]可正可负，所以得到的left，right大小关系不确定
            dp[i][0] = max(left, right, nums[i])
            dp[i][1] = min(left, right, nums[i])
            res = max(res, dp[i][0])
        return res