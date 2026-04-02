class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_count = Counter(nums)
        
        for num, count in nums_count.items():
            if count > 1:
                return True

        return False