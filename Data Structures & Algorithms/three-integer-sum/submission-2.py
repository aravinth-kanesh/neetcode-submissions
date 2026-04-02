class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            # do not want duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1
            # not <= because we don't want repeated elems in a trip
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # sorted order so increment left to make total bigger
                if total < 0:
                    left += 1
                # total too big so decrement right pointer
                elif total > 0:
                    right -= 1
                # valid triplet found
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # don't want dupes
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # right pointer correction handled by selection construct

        return res