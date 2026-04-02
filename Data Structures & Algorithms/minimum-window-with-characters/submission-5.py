class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        # create hashmaps for the window as well as the string t
        window, countT = {}, {}

        # populate hashmap with occurrance of characters in t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # res stores the indices of the mindow window substring
        # resLen stores the length of the mindow window - initialised to infinity
        # so that any real number will be less than it
        res, resLen = [-1, -1], float("infinity")
        
        # have is how many letters; occurences in the window match the occurrence
        # of the corresponding letter in the string t
        have, need = 0, len(countT)

        # initialise sliding window - left is a variable, right is in the
        # for loop
        left = 0
        for right in range(len(s)):
            # increment count of character at the right pointer
            c = s[right]
            window[c] = 1 + window.get(c, 0)

            # if the new count matches the required count according to
            # countT, then increment have
            if c in countT and window[c] == countT[c]:
                have += 1

            # loop while the window is valid
            # we want to shrink it as much as possible
            while have == need:
                # update res and resLen incase current window is new min
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                # shrink window from left, try to finding smaller valid window
                window[s[left]] -= 1

                # decrement have if condition is no longer met
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1

                # increment left pointer to complete window shrinking
                left += 1

        left, right = res
        return s[left: right + 1] if resLen != float("infinity") else ""


                

        