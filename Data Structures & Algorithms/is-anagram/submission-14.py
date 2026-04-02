class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # must be exact same characters and exact number of each
        return Counter(s) == Counter(t)