class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        #
        wordDict = set(wordDict)
        path=[]

        def dfs(startidx):
            if startidx == len(s):
                res.append(" ".join(path))
                return
            for i in range(startidx, len(s) + 1):
                if s[startidx:i] in wordDict:
                    path.append(s[startidx:i])
                    dfs(i)
                    path.pop()
                    #
        dfs(0)
        return res