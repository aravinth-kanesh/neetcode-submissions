class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        max_length = max_freq = 0
        
        left = 0
        for right in range(len(s)):
            window[s[right]] += 1
            max_freq = max(max_freq, window[s[right]])

            while (right - left + 1) - max_freq > k:
                window[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length