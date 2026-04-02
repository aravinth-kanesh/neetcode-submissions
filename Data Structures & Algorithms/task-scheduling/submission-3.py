class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)
        heap = [-frequency for frequency in frequencies.values()]
        heapq.heapify(heap)

        cycles = 0
        queue = deque()

        while heap or queue:
            if not heap:
                cycles = queue[0][1]
            else:
                cycles += 1
                frequency = 1 + heapq.heappop(heap)
                
                if frequency:
                    queue.append((frequency, cycles + n))

            if queue and cycles == queue[0][1]:
                heapq.heappush(heap, queue.popleft()[0])

        return cycles