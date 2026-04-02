class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, columns = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = row + dc, col + dr

                    if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        q.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands