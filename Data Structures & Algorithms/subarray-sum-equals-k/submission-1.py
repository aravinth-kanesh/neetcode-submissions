class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = count = 0
        seen = defaultdict(int)
        seen[0] = 1

        for num in nums:
            count += num

            if count - k in seen:
                total += seen[count - k]

            seen[count] += 1

        return total