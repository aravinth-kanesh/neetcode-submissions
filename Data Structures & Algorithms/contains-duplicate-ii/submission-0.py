class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        # cannot have a duplicate with only one number
        if n == 1:
            return False

        # no duplicates, not possible
        if n == len(set(nums)):
            return False

        indices = defaultdict(list)

        for i in range(n):
            # appends indices in linear order
            indices[nums[i]].append(i)

        # looks at the keys of the defaultdict
        for num in indices:
            freq = len(indices[num])
            # no duplicates of that number
            if freq == 1:
                continue

            # if we have [0, 2, 4], stop at len - 1
            for i in range(freq - 1):
                if indices[num][i + 1] - indices[num][i] <= k:
                    return True
        
        # return True line never reached
        return False
            
