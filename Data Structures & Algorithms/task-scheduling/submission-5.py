class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_count = Counter(tasks)

        heap = [-freq for freq in tasks_count.values()]
        heapq.heapify(heap) # max heap

        queue = deque() # (time_when_available, remaining_freq)

        time = 0

        while heap or queue:
            time += 1

            # add back task now available
            if queue and time == queue[0][0]:
                _, freq = queue.popleft()
                heapq.heappush(heap, -freq)

            # execute task
            if heap:
                freq = -heapq.heappop(heap)
                freq -= 1

                if freq > 0:
                    queue.append((time + n + 1, freq))

        return time