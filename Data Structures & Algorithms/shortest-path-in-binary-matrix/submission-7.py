class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        directions = [(r, c) for r in range(-1, 2) for c in range(-1, 2) if not (r == 0 and c == 0)]

        queue = deque([(0, 0, 1)])
        print([(r, c) for r, c, l in queue])
        grid[0][0] = 1

        while queue:
            row, column, length = queue.popleft()

            if (row, column) == (n - 1, n - 1):
                return length

            for dr, dc in directions:
                nr, nc = row + dr, column + dc
                print((nr, nc))

                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    queue.append((nr, nc, length + 1))
                    print([(r, c) for r, c, l in queue])

        return -1