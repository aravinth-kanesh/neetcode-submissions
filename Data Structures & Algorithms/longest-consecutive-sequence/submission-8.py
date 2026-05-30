class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums) # for efficient membership checks
        longest = 0

        for num in nums:
            if num - 1 not in nums_set: # start of a consecutive sequence  
                length = 1
                cur = num
                while cur + 1 in nums_set:
                    length += 1
                    cur += 1
                longest = max(longest, length)

        return longest