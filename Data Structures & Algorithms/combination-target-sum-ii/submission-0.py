class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        path=[]
        cur_sum=0
        candidates.sort()
        def traversal(candidates, target, startindex):
            nonlocal cur_sum
            if cur_sum==target:
                result.append(path[:])
                return
            if cur_sum > target:
                return
            for i in range(startindex,len(candidates)):
                if i>startindex and candidates[i]==candidates[i-1]:#所以这里i>startindex很重要，是允许1，1竖着取，防止1，1横着
                    continue
                cur_sum+=candidates[i]
                path.append(candidates[i])
                traversal(candidates,target,i+1)
                path.pop()
                cur_sum-=candidates[i]
        traversal(candidates,target,0)
        return result