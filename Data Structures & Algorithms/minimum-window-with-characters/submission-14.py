class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # get frequencies of every character in both strings
        s_count, t_count = defaultdict(int), Counter(t)

        # calculate unique characters required e.g., t in example
        # 1 has 3 - substring of s must have all 3 characters with 
        # at least the same frequency
        have, need = 0, len(t_count)

        # store the result and length of the result (to check if
        # subsequent valid substrings are shorter/longer)
        res, res_len = "", float('inf')

        left = 0
        for right in range(len(s)):
            # add character at right pointer to window
            char = s[right]
            s_count[char] += 1

            # same frequency of a particular character
            if char in t_count and s_count[char] == t_count[char]:
                have += 1
                print(f"have: {have}")

            # check if valid substring found - keep shrinking window
            # from left to find shorter valid substring
            while have == need:
                # calculate length of substring and update res
                if (right - left + 1) < res_len:
                    res = s[left:right + 1]
                    res_len = right - left + 1

                char = s[left]
                s_count[char] -= 1

                # frequency no longer matched
                if char in t_count and s_count[char] == t_count[char] - 1:
                    have -= 1

                # move left pointer forward
                left += 1

        return res if res_len != float('inf') else ""

                
