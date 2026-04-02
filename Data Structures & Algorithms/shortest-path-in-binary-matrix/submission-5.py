class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        n = len(grid)

        if grid[0][0] or grid[n - 1][n - 1]:
            return -1

        if n == 1:
            return 1

        queue = deque([(0, 0)])
        grid[0][0] = 1

        directions = [(x, y) for x in range(-1, 2) for y in range(-1, 2) if not (x == 0 and y == 0)]
        
        length = 0

        while queue:
            length += 1

            for _ in range(len(queue)):
                row, column = queue.popleft()

                if (row, column) == (n - 1, n - 1):
                    return length

                for dr, dc in directions:
                    new_row, new_column = row + dr, column + dc

                    if 0 <= new_row < n and 0 <= new_column < n and grid[new_row][new_column] == 0:
                        grid[new_row][new_column] = 1
                        queue.append((new_row, new_column))

        return -1