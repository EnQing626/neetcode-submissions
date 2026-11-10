class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        numA=numB=None
        cntA=cntB=0
        for num in nums:
            if num==numA:
                cntA+=1
            elif num==numB:
                cntB+=1
            elif numA is None:
                numA=num
                cntA+=1
            elif numB is None:
                numB=num
                cntB+=1
            else:
                cntA-=1
                cntB-=1
                if not cntA:
                    numA=None
                if not cntB:
                    numB=None
        cntA=cntB=0
        ans=[]
        for num in nums:
            if num==numA:
                cntA+=1
            elif num==numB:
                cntB+=1
        s=len(nums)//3
        if cntA>s:
            ans.append(numA)
        if cntB>s:
            ans.append(numB)
        return ans