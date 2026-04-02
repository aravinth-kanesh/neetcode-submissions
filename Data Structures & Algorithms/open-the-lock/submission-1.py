class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)

        if "0000" in dead:
            return -1

        queue = deque([("0000", 0)])
        visited = {"0000"}

        while queue:
            wheel_str, moves = queue.popleft()

            if wheel_str == target:
                return moves

            for i in range(4):
                slot = int(wheel_str[i])

                slot_up = str((slot + 1) % 10)
                slot_down = str((slot - 1) % 10)

                wheel_up = wheel_str[:i] + slot_up + wheel_str[i + 1:]
                wheel_down = wheel_str[:i] + slot_down + wheel_str[i + 1:]

                if wheel_up not in visited and wheel_up not in dead:
                    visited.add(wheel_up)
                    queue.append((wheel_up, moves + 1))
                
                if wheel_down not in visited and wheel_down not in dead:
                    visited.add(wheel_down)
                    queue.append((wheel_down, moves + 1))

        return -1