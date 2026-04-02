class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        r, c = len(matrix), len(matrix[0])

        left, right = 0, r * c - 1
        while left <= right:
            mid = (left + right) // 2
            row, column = mid // c, mid % c
            if target < matrix[row][column]:
                right = mid - 1
            elif target > matrix[row][column]:
                left = mid + 1
            else:
                return True

        return False