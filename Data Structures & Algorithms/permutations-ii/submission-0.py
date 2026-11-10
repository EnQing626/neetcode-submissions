class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]
        visited=[False]*len(nums)
        nums.sort()
        def traversal(nums):
            nonlocal path
            if len(path)==len(nums):
                result.append(path[:])
            for i in range(len(nums)):
                if visited[i]==True:
                    continue
                if i>0 and nums[i-1]==nums[i] and visited[i-1]==False:
                    continue
                path.append(nums[i])
                visited[i]=True
                traversal(nums)
                visited[i]=False
                path.pop()
        traversal(nums)
        return result