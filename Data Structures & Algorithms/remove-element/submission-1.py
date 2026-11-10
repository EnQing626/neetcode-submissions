class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:
            return 0
        l=0
        r=len(nums)-1
        while l<r:
            while (l<r and nums[l]!=val):
                l+=1
            while (l<r and nums[r]==val):
                r-=1
            nums[l],nums[r]=nums[r],nums[l]
        if nums[l]==val:
            return l
        return l+1