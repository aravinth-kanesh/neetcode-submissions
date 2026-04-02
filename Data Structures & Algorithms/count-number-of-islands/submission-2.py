class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # the idea behind this problem is to loop through every square
        # until a land is found. Then use BFS to search the whole island
        # , whilst making to mark all visited squares
        islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            visited.add((r, c))
            while queue:
                row, column = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, column + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '1' and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        queue.append((nr, nc))
        # main loop
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    islands += 1
                    bfs(r, c)

        return islands

        