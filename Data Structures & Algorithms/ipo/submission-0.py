class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        # 将profits和capital组合起来，并按本金排序，这样保证我们总能选取所有小于等于当前资本的
        projects = sorted(zip(profits, capital), key=lambda x:x[1])
        cur = []
        idx = 0
        while k:
            # 将所有需要的本金小于等于当前资本的项目加入最大堆
            while idx < n and projects[idx][1] <= w:
                heapq.heappush(cur, -projects[idx][0])
                idx += 1
            # 如果有项目在当前的大顶堆中，我们做利益最大的那一个。
            if cur:
                w -= heapq.heappop(cur)
            else:
                break
            k -= 1
        return w