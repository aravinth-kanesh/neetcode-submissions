class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count_s1 = Counter(s1)
        window = defaultdict(int) # char -> frequency

        for i in range(len(s1)):
            window[s2[i]] += 1

        if window == count_s1:
            return True

        for i in range(len(s1), len(s2)):
            # slide the window
            window[s2[i]] += 1
            window[s2[i - len(s1)]] -= 1

            # clean up hashmap if needed
            if window[s2[i - len(s1)]] == 0:
                del window[s2[i - len(s1)]]

            # check equality
            if window == count_s1:
                return True

        return False