class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]
        def traversal(nums,startidx):
            result.append(path[:])
            if startidx>=len(nums):
                return
            for i in range(startidx,len(nums)):
                path.append(nums[i])
                traversal(nums,i+1)
                path.pop()
        traversal(nums,0)
        return result