class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True) # sort from closest to destination to furthest
        stack = []

        for p, s in pairs:
            time = (target - p) / s
            stack.append(time)

            # car joins fleet
            if len(stack) >= 2 and time <= stack[-2]:
                stack.pop()

        return len(stack)