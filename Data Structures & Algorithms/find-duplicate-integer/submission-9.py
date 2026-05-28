class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # if the loop encounters a negative index, that means it has
        # already been seen in the array before
        for num in nums:
            index = abs(num) - 1

            if nums[index] < 0:
                return abs(num)

            nums[index] *= -1