class TimeMap:
    def __init__(self):
        self.store = defaultdict(list) # key -> list of (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.store[key]
        n = len(lst)
        left, right = 0, n - 1
        res = ""

        while left <= right:
            mid = (left + right) // 2

            # maybe larger prev_timestamp <= timestamp exists
            if lst[mid][0] <= timestamp:
                res = lst[mid][1] # get the value
                left = mid + 1
            # valid timestamp not found yet
            else:
                right = mid - 1

        return res