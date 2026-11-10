class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results=[]
        path=[]
        num_sum=0
        def traversal(candidates, target, startindex):
            nonlocal num_sum
            if num_sum>target:
                return
            if num_sum==target:
                results.append(path[:])
                return
            for i in range(startindex,len(candidates)):
                num_sum+=candidates[i]
                path.append(candidates[i])
                traversal(candidates,target,i)
                num_sum-=candidates[i]
                path.pop()
        traversal(nums,target,0)
        return results