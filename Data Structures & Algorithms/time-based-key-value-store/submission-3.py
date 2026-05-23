class TimeMap:
    def __init__(self):
        # maps key -> [(val, timestamp) pairs]
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))
        print(list(self.store.items()))

    def get(self, key: str, timestamp: int) -> str:
        val = ""

        for v, ts in self.store[key]:
            if ts <= timestamp:
                val = v
            else:
                break

        return val

        
