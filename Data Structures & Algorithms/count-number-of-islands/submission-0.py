class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))

            while queue:
                row, column = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                for dr, dc in directions:
                    nr, nc = row + dr, column + dc

                    if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        for r in range(rows):
            for c in range(columns):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands