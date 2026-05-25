class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # edge case
        if len(s1) > len(s2):
            return False

        window, count_s1 = defaultdict(int), Counter(s1)

        # populate window
        for ch in range(len(s1)):
            window[s2[ch]] += 1

        # initial window check
        if window == count_s1:
            return True

        for ch in range(len(s1), len(s2)):
            window[s2[ch]] += 1 # add new character
            window[s2[ch - len(s1)]] -= 1 # remove old character

            # clean up
            if window[s2[ch - len(s1)]] == 0:
                del window[s2[ch - len(s1)]]

            # check window again
            if window == count_s1:
                return True

        return False

        