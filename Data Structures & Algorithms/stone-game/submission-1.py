class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        N = len(piles)
        f = [[0]*(N+1) for _ in range(N+1)] # 防止出界
        for l in range(N):
            for i in range(N-l):
                j = i+l
                f[i][j] = max(piles[i]-f[i+1][j],
                              piles[j]-f[i][j-1])
        return f[0][N-1]>0