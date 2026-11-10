class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # 当前容量下多少天可以装完
        def helper(load):
            days = 1  # 最少也得花一天
            s = 0
            for x in weights:
                s += x
                if s > load:
                    days += 1
                    s = x  # 当前包开始新一天
            return days

        left = max(weights) # max(weights)是最小保证能装下所有weights的重量，但不保证在days内装完
        right = sum(weights) - 1 # sum(weights)肯定能在一天内装完，排除掉
        while left <= right: # 闭区间判断
            mid = (left + right) // 2
            if helper(mid) <= days:
                right = mid - 1
            else:
                left = mid + 1
        return left # 闭区间答案