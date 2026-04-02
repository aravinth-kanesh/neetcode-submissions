class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        window, countT = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")

        left = 0
        for right in range(len(s)):
            right_elem = s[right]
            window[right_elem] = 1 + window.get(right_elem, 0)

            if right_elem in countT and window[right_elem] == countT[right_elem]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1

        left, right = res
        return s[left : right + 1] if resLen != float("infinity") else ""

