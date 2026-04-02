# the idea behind this problem is to sort the cars closest to the target
# to furthest
# this allows cars behind that catch up to merge into a single fleet
# initialise a stack to store the time each car/fleet reaches the target
# compare the current car with the previous car/fleet - the one ahead 
# of it. If the time is smaller or equal to the one ahead of it,
# merge the fleets, as the car behind is faster than the fleet ahead
# the length of the stack at the end is how many fleets there are
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        pair.sort(reverse = True)

        stack = []

        for p, s in pair:
            stack.append((target - p) / s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)

        