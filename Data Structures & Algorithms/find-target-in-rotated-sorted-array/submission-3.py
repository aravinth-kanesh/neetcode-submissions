class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        print(f"Left: {left}, Right: {right}")

        while left <= right:
            mid = (left + right) // 2
            print(f"Mid: {nums[mid]}")

            # found target
            if nums[mid] == target:
                return mid
            # mid in left sorted portion
            elif nums[mid] >= nums[left]:
                # target in left sorted portion
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # mid in right sorted portion
            else:
                # target in right sorted portion
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # target in left sorted portion
                else:
                    right = mid - 1

            print(f"Left: {left}, Right: {right}")

        return -1


