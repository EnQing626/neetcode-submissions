class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        bagsize=len(s)+1
        dp=[False]*bagsize
        dp[0]=True
        for j in range(1,bagsize):
            for word in wordDict:
                if j>=len(word):
                    dp[j]=dp[j] or (dp[j-len(word)] and s[j-len(word):j]==word)
        print(dp)
        return dp[-1]