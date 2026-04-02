class TimeMap:
    def __init__(self):
        # hash table with map key --> [(value1, timestamp1), ()]
        # use defaultdict for coding ease
        self.h = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.h[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.h[key]
        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return res
