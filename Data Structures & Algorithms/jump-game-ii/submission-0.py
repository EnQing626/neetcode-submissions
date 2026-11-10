class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        ans = 0
        curDistance = 0
        nextDistance = 0
        for i in range(len(nums)):
            nextDistance = max(i + nums[i], nextDistance)  # 更新下一步覆盖最远距离下标
            if i == curDistance:                            #遇到当前覆盖最远距离下标
                if curDistance != len(nums) - 1:            #如果当前覆盖最远距离下标不是终点
                    ans += 1                                #需要走下一步
                    curDistance = nextDistance              #更新当前覆盖最远距离下标（相当于加油了）
                    if nextDistance >= len(nums) - 1:
                        break
                else:
                    break
        return ans