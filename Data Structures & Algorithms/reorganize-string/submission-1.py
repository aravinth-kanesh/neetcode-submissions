class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = Counter(s)

        heap = [(-freq, char) for char, freq in char_count.items()]
        heapq.heapify(heap)

        res = ""
        queue = deque() # (time_when_available, freq, char)
        time = 0

        while heap or queue:
            time += 1

            # can be readded to the heap
            if queue and queue[0][0] == time:
                _, freq, char = queue.popleft()
                heapq.heappush(heap, (freq, char))
            
            # impossible
            if not heap:
                return ""

            freq, char = heapq.heappop(heap)
            res += char
            freq += 1

            if freq < 0:
                queue.append((time + 2, freq, char))

        return res

            



