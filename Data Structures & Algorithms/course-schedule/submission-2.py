class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0 for _ in range(numCourses)]
        adjacency=collections.defaultdict(list)
        queue=deque()
        for cur,pre in prerequisites:
            indegree[cur]+=1
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not indegree[i]:
                queue.append(i)
        while queue:
            pre=queue.popleft()
            numCourses-=1
            for cur in adjacency[pre]:
                indegree[cur] -= 1
                if not indegree[cur]:
                    queue.append(cur)
        return not numCourses