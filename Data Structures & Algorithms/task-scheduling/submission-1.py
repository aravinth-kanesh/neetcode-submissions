class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_frequency = Counter(tasks)
        heap = [-f for f in task_frequency.values()]
        heapq.heapify(heap)

        cycles = 0
        queue = deque()

        while heap or queue:

            if not heap:
                cycles = queue[0][1]
            else:
                cycles += 1
                frequency = 1 + heapq.heappop(heap)  # reduce count

                if frequency:
                    queue.append((frequency, cycles + n))

            if queue and queue[0][1] == cycles:
                heapq.heappush(heap, queue.popleft()[0])

        return cycles