class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, columns = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        queue = deque()
        fresh = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r, c, 0))

        if fresh == 0:
            return 0

        while queue and fresh:
            r, c, time = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < columns and grid[nr][nc] == 1:
                    fresh -= 1

                    if fresh == 0:
                        return time + 1

                    grid[nr][nc] = 2
                    queue.append((nr, nc, time + 1))

        return -1

                    