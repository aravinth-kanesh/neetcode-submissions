class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = []
        i = j = 0

        # Merge both arrays
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                combined.append(nums1[i])
                i += 1
            else:
                combined.append(nums2[j])
                j += 1

        # Add remaining elements
        combined.extend(nums1[i:])
        combined.extend(nums2[j:])

        n = len(combined)
        mid = n // 2

        # Compute median
        if n % 2 == 1:
            return float(combined[mid])
        else:
            return (combined[mid - 1] + combined[mid]) / 2
