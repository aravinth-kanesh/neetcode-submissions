class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count_s1, window = Counter(s1), defaultdict(int)

        for i in range(len(s1)):
            window[s2[i]] += 1

        if window == count_s1:
            return True

        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1
            window[s2[i - len(s1)]] -= 1

            if window[s2[i - len(s1)]] == 0:
                del window[s2[i - len(s1)]]

            if window == count_s1:
                return True

        return False