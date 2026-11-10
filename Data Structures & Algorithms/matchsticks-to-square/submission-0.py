class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4: return False
        div, mod = divmod(sum(matchsticks), 4)
        if mod != 0:
            return False
        matchsticks.sort(reverse=True)
        edges = [0] * 4

        def dfs(i):
            if i == len(matchsticks):
                if len(set(edges)) == 1:
                    return True
                return False
            for k in range(4):
                if edges[k] + matchsticks[i] > div: continue
                edges[k] += matchsticks[i]
                if dfs(i + 1): return True
                edges[k] -= matchsticks[i]
            return False
        return dfs(0)