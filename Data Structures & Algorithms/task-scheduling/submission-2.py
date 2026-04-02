class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)
        heap = [-frequency for frequency in frequencies.values()]
        heapq.heapify(heap)

        # stores (frequency, time when available)
        queue = deque()
        cycles = 0

        while heap or queue:
            if not heap:
                # set time to next task
                cycles = queue[0][1]
            else:
                cycles += 1
                frequency = 1 + heapq.heappop(heap) # decrement frequency
                
                # still more tasks
                if frequency:
                    queue.append((frequency, cycles + n))

            # add task that is now available back to the heap
            if queue and cycles == queue[0][1]:
                heapq.heappush(heap, queue.popleft()[0])

        return cycles
