class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            index = abs(nums[i]) - 1

            if nums[index] < 0:
                return abs(nums[i])
            
            nums[index] *= -1
