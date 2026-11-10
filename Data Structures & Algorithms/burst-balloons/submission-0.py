class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # 补1
        nums = [1] + nums + [1]
        # 状态定义+初始化
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for size in range(3, n+1): # 从小窗口递推到大窗口，开区间所以窗口长度最小为3
            for start in range(n-size+1):
                end = start + size - 1 # start和end构成一个开区间窗口
                ma = 0
                for k in range(start+1, end): # k为start~end开区间内的最后一个气球,注意开区间
                    cur_k = dp[start][k] + nums[start] * nums[k] * nums[end] + dp[k][end]# 最后一个气球只与边界有关
                    ma = max(ma, cur_k)
                dp[start][end] = ma # 更新此区间的最多金币为k取不同位置时的金币最大值
        return dp[0][n-1]