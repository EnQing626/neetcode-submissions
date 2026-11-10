class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        from collections import defaultdict
        graph=defaultdict(dict)
        for (a,b),v in zip(equations,values):
            graph[a][b]=v
            graph[b][a]=1/v
        def dfs(s,e):
            if s not in graph or e not in graph:
                return -1
            if s==e:
                return 1
            visited.add(s)
            for i in graph[s]:
                if i==e:
                    return graph[s][i]
                if i not in visited:
                    ans=dfs(i,e)
                    if ans!=-1:
                        return graph[s][i]*ans
            return -1
        res=[]
        for a,b in queries:
            visited=set()
            res.append(dfs(a,b))
        return res