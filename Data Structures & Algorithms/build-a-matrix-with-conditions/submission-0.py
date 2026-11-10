class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        n, m = len(rowConditions), len(colConditions)
        
        def findOrder(k: int, cond: List[List[int]]):
            edges = defaultdict(list)
            indeg = defaultdict(int)

            result = []

            for u, v in cond:
                edges[u].append(v)
                indeg[v] += 1

            que = deque(
                [u for u in range(1, k + 1) if indeg[u] == 0]
            )

            while que:
                u = que.popleft()
                result.append(u)
                
                for v in edges[u]:
                    indeg[v] -= 1

                    if indeg[v] == 0:
                        que.append(v)

            if len(result) != k:
                result = []
                
            return result
        
        rows = findOrder(k, rowConditions)
        cols = findOrder(k, colConditions)
        
        if not rows or not cols:
            return []
        
        num2row = {
            num: row for row, num in enumerate(rows)
        }
        num2col = {
            num: col for col, num in enumerate(cols)
        }
         
        res = [[0 for _ in range(k)] for _ in range(k)]

        # *** 这里我又想多了 ***

        # rset = set(range(k)) - set(rows)
        # cset = set(range(k)) - set(cols)
        
        # for num in range(1, k + 1):
        #     if num in num2row:
        #         row = num2row[num]
        #     else:
        #         row = rset.pop()
                        
        #     if num in num2col:
        #         col = num2col[num]
        #     else:
        #         col = cset.pop()
                
        #     res[row][col] = num

        for num in range(1, k + 1):
            row, col = num2row[num], num2col[num]
            res[row][col] = num
        
        return res