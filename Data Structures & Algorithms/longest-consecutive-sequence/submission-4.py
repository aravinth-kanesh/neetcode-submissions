class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest = 1
        
        for num in nums:
            if num - 1 not in nums:
                curr = num
                current_longest = 1
                while curr + 1 in nums:
                    current_longest += 1
                    curr += 1
                    longest = max(longest, current_longest)

        return longest
