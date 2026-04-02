class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, columns = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visited = set()

        queue = deque()   
        for r in range(rows):
            for c in range(columns):
                if (r == 0 or r == rows - 1 or c == 0 or c == columns - 1) and board[r][c] == "O":
                    board[r][c] = "Z"
                    queue.append((r, c))

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < columns and board[nr][nc] == "O":
                    board[nr][nc] = "Z"
                    queue.append((nr, nc))

        for r in range(rows):
            for c in range(columns):
                # stays as O
                if board[r][c] == "Z":
                    board[r][c] = "O"

                # surrounded - flip
                elif board[r][c] == "O":
                    board[r][c] = "X"

        