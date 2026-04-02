class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_occ = {}

        for num in nums:
            if num in nums_occ:
                return True

            nums_occ[num] = 1
            
        return False
        