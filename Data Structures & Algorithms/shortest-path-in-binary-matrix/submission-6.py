class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # n x n matrix, so same number of rows and columns
        n = len(grid)

        # don't need to check for empty grid edge case

        # check if start or end are blocked, if so, impossible
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        # we will use bfs, which gives us the shortest path in
        # an unweighted graph

        # length is number of visited cells of this path, so start
        # length is 1

        # queue for bfs approach
        # (row, column, length)
        queue = deque([(0, 0, 1)])
        grid[0][0] = 1
        print([(r, c, l) for r, c, l in queue])

        # define all 8 directions
        directions = [(r, c) for r in range(-1, 2) for c in range(-1, 2) if not (r == 0 and c == 0)]
        
        while queue:
            row, column, length = queue.popleft()

            # end reached
            if (row, column) == (n - 1, n - 1):
                return length

            # explore all 8 directions 
            for dr, dc in directions:
                nr, nc = row + dr, column + dc
                print((nr, nc))

                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                    # mark as visited by overriding matrix
                    grid[nr][nc] = 1
                    queue.append((nr, nc, length + 1))
                    print([(r, c, l) for r, c, l in queue])

        # if inner return statement not reached, not possible to reach end
        return -1

            