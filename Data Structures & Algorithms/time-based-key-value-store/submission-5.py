class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        value = ""
        lst = self.store[key]

        left, right = 0, len(lst) - 1
        while left <= right:
            mid = (left + right) // 2

            if lst[mid][0] <= timestamp:
                value = lst[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        return value
