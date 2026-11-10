class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(s,i,j):
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            return i+1,j-1
        start,end=0,0
        for i in range(len(s)):
            left1,right1=expand(s,i,i)
            left2,right2=expand(s,i,i+1)
            if right1-left1>end-start:
                end=right1
                start=left1
            if right2-left2>end-start:
                end=right2
                start=left2
        return s[start:end+1]