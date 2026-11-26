class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results=[]
        path=[]
        
        def traversal(nums, startindex):
            nonlocal results
            #nonlocal path
            results.append(path[:])
            if startindex>=len(nums):
                return
            for i in range(startindex,len(nums)):
                path.append(nums[i])
                traversal(nums,i+1)
                path.pop()

        traversal(nums, 0)
        return results