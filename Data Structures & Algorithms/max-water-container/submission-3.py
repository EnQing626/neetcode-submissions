class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res=0
        left=0
        right=len(heights)-1
        while left<right:
            cur_res=(right-left)*min(heights[left],heights[right])
            res=max(res,cur_res)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return res