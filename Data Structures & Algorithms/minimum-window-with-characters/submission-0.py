class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ''
        cnt=collections.Counter(t)
        need=len(t)
        start,end=0,-1
        left=right=0
        min_len=len(s)+1
        for right in range(len(s)):
            c1=s[right]
            if c1 in cnt:
                if cnt[c1]>0:
                    need-=1
                cnt[c1]-=1
            while need==0:
                if right-left+1<min_len:
                    min_len=right-left+1
                    start,end=left,right
                c2=s[left]
                if c2 in cnt:
                    if cnt[c2]==0:
                        need+=1
                    cnt[c2]+=1
                left+=1
        return s[start:end+1]