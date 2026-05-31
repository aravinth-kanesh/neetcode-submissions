class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        left = longest = max_freq = 0

        for right in range(len(s)):
            window[s[right]] += 1
            max_freq = max(max_freq, window[s[right]])

            while (right - left + 1) - max_freq > k:
                window[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest
