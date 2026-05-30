class TimeMap:
    def __init__(self):
        self.store = defaultdict(list) # key -> (timestamp, value) pairs

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # set() was called previously, so len(self.store[key]) >= 1
        lst = self.store[key]
        res = ""

        # binary search to find the largest valid timestamp
        left, right = 0, len(lst) - 1
        while left <= right:
            mid = (left + right) // 2

            if lst[mid][0] <= timestamp:
                # update result
                res = lst[mid][1]

                # may find a larger valid timestamp
                left = mid + 1
            else:
                # haven't found a valid timestamp yet
                right = mid - 1

        return res