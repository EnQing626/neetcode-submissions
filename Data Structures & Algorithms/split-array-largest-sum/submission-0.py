class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mx: int) -> bool:
            cnt = 1
            s = 0
            for x in nums:
                if s + x <= mx:
                    s += x
                else:
                    cnt += 1
                    s = x
                    if cnt > k:
                        return False
            return True
        left = max(nums)
        right = sum(nums)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid        # 记录当前可行解
                right = mid - 1  # 收缩右边
            else:
                left = mid + 1   # 收缩左边
        return ans