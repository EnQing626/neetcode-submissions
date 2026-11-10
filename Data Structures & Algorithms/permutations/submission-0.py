class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        path=[]
        visited=[False]*len(nums)
        def traversal(nums):
            if len(path)==len(nums):
                result.append(path[:])
            for i in range(len(nums)):
                if visited[i]==True:
                    continue
                path.append(nums[i])
                visited[i]=True
                traversal(nums)
                visited[i]=False
                path.pop()
        traversal(nums)
        return result