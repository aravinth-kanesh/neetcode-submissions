class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        max_length = 0
        
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            freq = max(window.values())

            while (right - left + 1) - freq > k:
                window[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length