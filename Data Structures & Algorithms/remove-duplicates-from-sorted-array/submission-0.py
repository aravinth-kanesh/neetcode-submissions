class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[curr] = nums[i - 1]
                curr += 1
        
        nums[curr] = nums[-1]
        return curr + 1
