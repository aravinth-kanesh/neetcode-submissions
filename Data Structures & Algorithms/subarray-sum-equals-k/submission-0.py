class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # count is num of subarrays that sum to k
        # prefix sum is the sum of elements before the current
        count = prefix_sum = 0
        # maps prefix sum --> number of times sum seen
        seen = defaultdict(int)
        # prefix sum of 0 is automatically true and has been "seen"
        seen[0] = 1

        # the idea behind this problem is that:
        # if current prefix - previous prefix sum = k,
        # then subarray from start of previous prefix sum to current
        # element is equal to k

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in seen:
                count += seen[prefix_sum - k]

            seen[prefix_sum] += 1

        return count