class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        count_s1, window = Counter(s1), defaultdict(int)

        for i in range(len(s1)):
            window[s2[i]] += 1

        if window == count_s1:
            return True

        for i in range(len(s1), len(s2)):
            window[s2[i]] += 1
            left_char = s2[i - len(s1)]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            if window == count_s1:
                return True

        return False
