class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queue = []
        distance = lambda x: points[x][0]**2 + points[x][1]**2
        length = len(points)
        for i in range(length):
            heapq.heappush(queue, (distance(i), points[i]))
        res = []
        for i in range(k):
            res.append(heapq.heappop(queue)[1])
        return res