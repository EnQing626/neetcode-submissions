class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans=[]
        i,n,m=0,len(word1),len(word2)
        while i<n or i<m:
            if i<n:
                ans.append(word1[i])
            if i<m:
                ans.append(word2[i])
            i+=1
        return "".join(ans)