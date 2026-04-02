class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # return true if the array has duplicates
        # this is when len(set(nums)) is less than len(nums)
        return len(set(nums)) < len(nums)