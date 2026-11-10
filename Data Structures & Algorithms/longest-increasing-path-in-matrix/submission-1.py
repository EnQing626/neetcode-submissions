from functools import lru_cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        #best=1
        DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        @lru_cache(None)
        def dfs(row: int, column: int) -> int:
            best = 1
            #nonlocal best
            for dx, dy in DIRS:
                newRow, newColumn = row + dx, column + dy
                if 0 <= newRow < rows and 0 <= newColumn < columns and matrix[newRow][newColumn] > matrix[row][column]:
                    best = max(best, dfs(newRow, newColumn) + 1)
            return best

        ans = 0
        rows, columns = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                ans = max(ans, dfs(i, j))
        return ans