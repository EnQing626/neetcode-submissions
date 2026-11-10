class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = n*[float('inf')]
        dist[src]=0
        for i in range(k+1):
            dist_old=[_ for _ in dist]
            for u,v,value in flights:
                dist[v]=min(dist[v],dist_old[u]+value)#!!!!!!注意dist_old
        return dist[dst] if dist[dst]!=float('inf') else -1