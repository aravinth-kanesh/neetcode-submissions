class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, columns = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()

        fresh, minutes = 0, 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c, 0))

        while queue:
            row, column, minute = queue.popleft()
            minutes = max(minutes, minute)

            for dr, dc in directions:
                nr, nc = row + dr, column + dc

                if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1:
                    fresh -= 1
                    grid[nr][nc] = 2
                    queue.append((nr, nc, minute + 1))

        return minutes if not fresh else -1


