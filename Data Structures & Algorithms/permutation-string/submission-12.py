class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # s2 has to be at least as long as s1 for it to be a possible perm
        if len(s2) < len(s1):
            return False

        count_s1 = Counter(s1)
        window = defaultdict(int) # char -> frequency

        # populate window to s1 size
        for i in range(len(s1)):
            window[s2[i]] += 1

        # check initial window
        if window == count_s1:
            return True

        # slide the window and iteratively check equality
        for j in range(len(s1), len(s2)):
            window[s2[j]] += 1
            window[s2[j - len(s1)]] -= 1
            
            # clean up hashmap (prevent zero counts from remaining)
            if window[s2[j - len(s1)]] == 0:
                del window[s2[j - len(s1)]]

            if window == count_s1:
                return True

        return False