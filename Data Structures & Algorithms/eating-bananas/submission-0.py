class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)  # 注意 left 不能从 0 开始，因为除数不能为 0
        result = right  # 记录最小满足条件的速度

        while left <= right:
            mid = (left + right) // 2
            total_hours = sum(math.ceil(p / mid) for p in piles)

            if total_hours <= h:
                result = min(result,mid)  # 满足条件，尝试更小的速度
                right = mid - 1
            else:
                left = mid + 1

        return result