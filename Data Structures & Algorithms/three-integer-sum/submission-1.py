class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        n=len(nums)
        for i in range(n):
            left=i+1
            right=n-1
            if nums[i]>0:
                break
            if i>=1 and nums[i-1]==nums[i]:
                continue
            while left<right:
                temp = nums[i]+nums[left]+nums[right]
                if temp<0:
                    left+=1
                elif temp>0:
                    right-=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    while left!=right and nums[left]==nums[left+1]:
                        left+=1
                    while left!=right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
        return res
