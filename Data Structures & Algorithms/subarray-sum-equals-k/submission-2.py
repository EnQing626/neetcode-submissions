class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        num_times=defaultdict(int)
        num_times[0]=1
        res=0
        cur_sum=0
        for i in range(len(nums)):
            cur_sum+=nums[i]
            if cur_sum-k in num_times:
                res+=num_times[cur_sum-k]
            num_times[cur_sum]+=1
        return res
