class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = arr[-1]
        arr[-1] = -1
        n = len(arr)

        if n == 1:
            return arr

        for i in range(n - 2, -1, -1):
            temp = arr[i]
            arr[i] = max_right
            max_right = max(max_right, temp)

        return arr