class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, columns = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        queue = deque()
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 0:
                    queue.append((r, c, 0))

        while queue:
            for _ in range(len(queue)):
                r, c, distance = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = distance + 1
                        queue.append((nr, nc, distance + 1))