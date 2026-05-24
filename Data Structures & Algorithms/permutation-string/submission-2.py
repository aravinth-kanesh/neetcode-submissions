class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if s1 is longer, impossible
        if len(s1) > len(s2):
            return False

        s1_len = len(s1)

        count_s1 = Counter(s1)
        window = defaultdict(int)

        # build initial window
        for i in range(s1_len):
            window[s2[i]] += 1

        # check first window
        if window == count_s1:
            return True

        for i in range(s1_len, len(s2)):
            # add new character
            window[s2[i]] += 1

            left_char = s2[i - s1_len]

            # remove old character
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            # check new window
            if window == count_s1:
                return True

        return False