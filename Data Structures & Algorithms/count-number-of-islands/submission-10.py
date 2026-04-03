class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        # determine number of rows and columns
        rows, columns = len(grid), len(grid[0])

        # track squares which have been visited
        visited = set()

        # explore in 4 directions
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # grid can never be empty, so don't need to check for that
        # edge case

        # strategy: iterate through each square in the grid - if an
        # unvisited land is encountered, run bfs on it to fully
        # explore the island and increment islands by 1. Return the
        # total number of islands at the end

        # bfs helper method
        def bfs(r, c):
            # queue for bfs implementation
            queue = deque([(r, c)])

            # mark the square as visited
            visited.add((r, c))

            # explore the whole island
            while queue:
                row, column = queue.popleft()

                # explore in all 4 directions
                for dr, dc in directions:
                    new_row, new_column = row + dr, column + dc

                    # ensure new square is within the bounds of the grid
                    # and hasn't been visited before
                    if 0 <= new_row < rows and 0 <= new_column < columns and grid[new_row][new_column] == "1" and (new_row, new_column) not in visited:
                        # mark it as visited and append it to the queue
                        visited.add((new_row, new_column))
                        queue.append((new_row, new_column))



        # main loop
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and (r, c) not in visited:
                    # explore the entire island and mark as visited
                    bfs(r, c)
                    islands += 1

        return islands

        # time is O(r x c) and space is O(r x c) in the worst case,
        # when the whole grid is one big island