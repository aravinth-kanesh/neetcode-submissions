class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        rows, columns = len(matrix), len(matrix[0])
        right = (rows * columns) - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // columns
            column = mid % columns
            val = matrix[row][column]

            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False