class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        L = n*[0]
        R = n*[0]
        answer=n*[0]
        L[0]=1
        R[n-1]=1
        for i in range(1,n):
            L[i]=L[i-1]*nums[i-1]
        for j in range(n-2,-1,-1):
            R[j]=R[j+1]*nums[j+1]
        for i in range(n):
            answer[i]=L[i]*R[i]
        return answer