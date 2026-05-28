class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] <= nums[right]:
                res = min(res, nums[left])
                break

            mid = (left + right) // 2
            res = min(res, nums[mid]) # update min possibly

            # left sorted portion - search in right
            if nums[mid] >= nums[left]:
                left = mid + 1
            # right sorted portion - search in left
            else:
                right = mid - 1

        return res
