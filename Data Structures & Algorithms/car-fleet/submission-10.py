class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True) # pairs[0] will be closest to the destination
        stack = []

        for p, s in pairs:
            time = (target - p) / s
            stack.append(time)

            if len(stack) >= 2 and time <= stack[-2]:
                stack.pop() # merge with fleet in front

        return len(stack)