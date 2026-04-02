class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # this is a multi-source BFS question

        rows, columns = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        queue = deque()
        visited = set()

        # add all treasure chest squares to the queue
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))

        while queue:
            for _ in range(len(queue)):
                r, c, d = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # only append unexplored land cells to the queue
                    if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = d + 1
                        queue.append((nr, nc, d + 1))


