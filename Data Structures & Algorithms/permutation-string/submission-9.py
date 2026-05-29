class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count_s1 = Counter(s1)
        print(f"s1: {count_s1}")
        window = defaultdict(int) # char -> frequency

        for i in range(len(s2)):
            if i < len(s1):
                window[s2[i]] += 1
                continue

            # window is correct size
            print(f"Window: {window}")
            if window == count_s1:
                return True

            # slide the window
            window[s2[i]] += 1
            window[s2[i - len(s1)]] -= 1
            print(f"Window: {window}")

            # clean up hashmap if needed
            if window[s2[i - len(s1)]] == 0:
                del window[s2[i - len(s1)]]

        return window == count_s1