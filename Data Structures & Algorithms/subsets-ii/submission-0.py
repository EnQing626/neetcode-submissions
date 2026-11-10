class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]
        nums.sort()
        def traversal(nums, startidx):
            result.append(path[:])
            if startidx>=len(nums):
                return
            for i in range(startidx,len(nums)):
                if i>startidx and nums[i-1]==nums[i]:
                    continue
                path.append(nums[i])
                traversal(nums,i+1)
                path.pop()
        traversal(nums,0)
        return result