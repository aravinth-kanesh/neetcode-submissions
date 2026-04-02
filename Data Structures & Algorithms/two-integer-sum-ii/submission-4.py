class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # the key to identifying the two pointers pattern here
        # is that the input array is sorted and we need to find
        # a pair that satisfies the condition

        left, right = 0, len(numbers) - 1

        # want unique numbers
        while left < right:
            total = numbers[left] + numbers[right]

            if total == target:
                # we add one as the it is asking for the 1-indexed version
                # check for solution first for quick return for 
                # efficiency before incrementing/decrementing pointers
                return [left + 1, right + 1]
            elif total < target:
                # increment left pointer as this will increase total
                # remember - the array is sorted
                left += 1
            else:
                # total is too big - decrement right to decrease total
                right -= 1

        # always one valid solution so return nothing outside of while