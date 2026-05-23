class TimeMap:
    def __init__(self):
        # maps key -> [(val, timestamp) pairs]
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        val = ""
        lst = self.store[key]

        # binary search approach
        left, right = 0, len(lst) - 1

        # do not allow pointers to move past each other
        while left <= right:
            mid = (left + right) // 2

            # lst[mid][1] gets the timestamp
            if lst[mid][1] <= timestamp:
                # update value
                val = lst[mid][0]

                # could be a larger valid timestamp
                left = mid + 1
            else:
                # valid timestamp not found
                right = mid - 1

        return val


        
