class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # start bfs from unvisited land to fully explore it
        # number of bfs calls is the number of islands

        islands = 0
        rows, columns = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def bfs(r, c):
            queue = deque([(r, c)])
            visited.add((r, c))

            # explore entire island and mark as visited
            while queue:
                row, column = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = row + dr, column + dc

                    if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == "1" and (nr, nc) not in visited:
                        queue.append((nr, nc))
                        visited.add((nr, nc))

        # main loop
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
