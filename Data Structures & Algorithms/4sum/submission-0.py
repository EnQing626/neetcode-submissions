class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        n=len(nums)
        nums.sort()
        for i in range(n):
            if nums[i]>target and (nums[i]>0 or target>0):
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            for k in range(i+1,n):
                if k>i+1 and nums[k]==nums[k-1]:
                    continue
                left=k+1
                right=n-1
                while left<right:
                    total=nums[i]+nums[k]+nums[left]+nums[right]
                    if total<target:
                        left+=1
                    elif total>target:
                        right-=1
                    else:
                        res.append([nums[i],nums[k],nums[left],nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
        return res