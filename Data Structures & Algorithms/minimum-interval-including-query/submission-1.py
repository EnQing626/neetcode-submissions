import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()  # 按左端点排序
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])  # (值, 原索引)
        res = [-1] * len(queries)
        min_heap = []  # 存储符合条件的区间 (长度, 右端点)

        i = 0  # interval 指针

        for q, idx in sorted_queries:
            # 先把所有左端点 <= q 的 interval 加入堆中
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                if r >= q:  # 只考虑能包含查询的区间
                    heapq.heappush(min_heap, (r - l + 1, r))
                i += 1

            # 把堆中所有右端点 < q 的区间踢出
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            if min_heap:
                res[idx] = min_heap[0][0]

        return res