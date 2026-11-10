class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n=len(s)
        left=right=0
        counter=collections.Counter()
        res=0
        while right<n:
            counter[s[right]]+=1
            while right-left+1-counter.most_common(1)[0][1]>k:
                counter[s[left]]-=1
                left+=1
            res=max(res,right-left+1)
            right+=1
        return res