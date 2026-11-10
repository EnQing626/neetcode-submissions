class Solution:

    def encode(self, strs: List[str]) -> str:
        ans=[]
        for s in strs:
            ans.append('{:4}'.format(len(s))+s)
        #print(ans)
        return ''.join(ans)
    def decode(self, s: str) -> List[str]:
        ans=[]
        i=0
        n=len(s)
        while i<n:
            size=int(s[i:i+4])
            i+=4
            temp=s[i:i+size]
            ans.append(temp)
            i+=size
        return ans