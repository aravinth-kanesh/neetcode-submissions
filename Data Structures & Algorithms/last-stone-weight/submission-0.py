class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # "no more than one stone remaining" - when there are
        # <= 1 stones, so either 1 or 0 stones

        # max_heap to store the weights of the stones
        # negate values to achieve max heap
        heap = [-weight for weight in stones]

        # turn the array into a heap
        heapq.heapify(heap)

        print([-weight for weight in heap])

        # keep running simulations until no more than one stone
        # remaining
        #
        # there must be at least 2 stones for a simulation
        while len(heap) >= 2:
            # either x and y have the same weight, or x < y
            # don't forget to negate values since this is a max heap
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            print(f"x: {x}, y: {y}")

            if x != y:
                # x is less than y, y remains with y - x weight
                heapq.heappush(heap, -(y - x))
                print(f"x destroyed, y remains with weight {y - x}")
            else:
                print("Both stones destroyed")

            print([-weight for weight in heap])

        # the heap will have either 1 or 0 stones left
        # at the end
        #
        # don't forget to negate values since this is a max heap
        return -heap[0] if heap else 0