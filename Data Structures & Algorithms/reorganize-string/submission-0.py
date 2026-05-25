class Solution:
    def reorganizeString(self, s: str) -> str:
        char_count = Counter(s) # {'a': 3, 'b': 4}
        heap = [(-freq, char) for char, freq in char_count.items()] # max heap
        heapq.heapify(heap)

        queue = deque() # (time_when_available, freq, char)
        res = []
        time = 0

        # if no char is popped from the heap in a specific time
        # step, then not possible
        while heap or queue:
            time += 1

            # character can appear in the sequence again
            if queue and time == queue[0][0]:
                _, freq, char = queue.popleft()
                heapq.heappush(heap, (-freq, char))
            
            if not heap:
                return ""

            neg_freq, char = heapq.heappop(heap)
            res.append(char) # add to result
            freq = -neg_freq - 1

            if freq > 0:
                # cannot be the next character
                queue.append((time + 2, freq, char))

        return "".join(res)


