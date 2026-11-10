class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        # 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if (
                    nr < 0
                    or nr >= rows
                    or nc < 0
                    or nc >= cols
                    or grid[nr][nc] != 2147483647
                ):
                    continue
                grid[nr][nc] = grid[r][c] + 1
                queue.append((nr, nc))