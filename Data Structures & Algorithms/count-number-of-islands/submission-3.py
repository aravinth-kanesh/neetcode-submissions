class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        if not grid:
            return islands

        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))

            while queue:
                row, column = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, column + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands