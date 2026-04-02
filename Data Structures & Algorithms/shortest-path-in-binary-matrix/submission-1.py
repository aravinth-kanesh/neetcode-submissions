class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # binary matrix tells me that it only consists of 1s and 0s
        # - makes edge cases easier - don't need to check for invalid input

        # key point - the length of the path in actually 1 + actual path

        # n x n matrix so number of rows and columns don't differ
        n = len(grid)

        # check if there exists a grid - another edge case
        if not grid:
            return -1

        # easy edge case - no possible path
        if grid[0][0] == 1 or grid[n - 1][n - 1] == 1:
            return -1

        # another edge case - check if the start is the end
        if n == 1:
            return 1

        # brute force - calculate the lengths of all possible clear paths
        # and then return the smallest one.

        # better solution - use bfs to find the shortest clear path.
        # since the graph is unweighted, the first time it returns a 
        # path will be the shortest path

        # optimisation - use a visited set to prevent squares from being
        # reprocessed, BUT i can avoid this extra spacd by modifying the 
        # grid squares

        # length of clear path
        length = 0

        # initialise the deque for BFS
        queue = deque([(0, 0)])
        
        # mark as visited
        grid[0][0] = 2

        # define all directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]

        while queue:
            length += 1

            for _ in range(len(queue)):
                row, column = queue.popleft()

                # we have reached the end
                if (row, column) == (n - 1, n - 1):
                    return length

                # exploring all neighbours
                for dr, dc in directions:
                    new_row, new_column = row + dr, column + dc

                    if 0 <= new_row < n and 0 <= new_column < n and grid[new_row][new_column] == 0:
                        grid[new_row][new_column] = 2 # prevent the square from being reprocessed
                        queue.append((new_row, new_column))

        # only reaches this point if a path hasn't been found
        return -1