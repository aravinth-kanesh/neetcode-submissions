class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        minutes = fresh = 0
        rows, columns = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append((r, c))

        while queue and fresh:
            minutes += 1

            for _ in range(len(queue)):
                row, column = queue.popleft()

                for dr, dc in directions:
                    new_row, new_column = row + dr, column + dc

                    if 0 <= new_row < rows and 0 <= new_column < columns and grid[new_row][new_column] == 1:
                        grid[new_row][new_column] = 2
                        fresh -= 1
                        queue.append((new_row, new_column))

        return minutes if not fresh else -1

