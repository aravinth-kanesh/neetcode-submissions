class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            index = abs(num) - 1
            if nums[index] < 0: # already seen before
                return abs(num)
            nums[index] *= -1
            print(nums)
                 